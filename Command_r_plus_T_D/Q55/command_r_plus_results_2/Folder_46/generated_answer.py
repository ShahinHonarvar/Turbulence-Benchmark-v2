def lists_with_product_equal_n(nums: list[int]) -> list[list[int]]:

    def product_equal_n(nums: list[int], n: int) -> list[list[int]]:
        result = []
        for i in range(len(nums)):
            product = 1
            temp = []
            for j in range(i, len(nums)):
                product *= nums[j]
                if product == n:
                    temp.append(nums[j])
                    result.append(temp[:])
                elif product > n:
                    break
        return result
    result = []
    for i in range(len(nums)):
        nums_copy = nums[i:] + nums[:i]
        result.extend(product_equal_n(nums_copy, 53))
    return result