def lists_with_product_equal_n(nums: list[int]) -> list[list[int]]:

    def product_equal_to_n(n: int, nums: list[int]) -> list[list[int]]:
        result = []
        for i in range(len(nums)):
            product = 1
            sublist = []
            for j in range(i, len(nums)):
                product *= nums[j]
                sublist.append(nums[j])
                if product == n:
                    result.append(sublist)
                if product > n:
                    break
        return result
    if not nums:
        return []
    result = product_equal_to_n(-1, nums)
    if result:
        return result
    for i in range(1, len(nums)):
        circular_nums = nums[-i:] + nums[:-i]
        result = product_equal_to_n(-1, circular_nums)
        if result:
            return result
    return []