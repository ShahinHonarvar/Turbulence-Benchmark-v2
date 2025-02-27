def lists_with_product_equal_n(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    result = []
    for i in range(n):
        for j in range(i, n + i):
            product = 1
            sublist = []
            for k in range(i, j % n + 1):
                product *= nums[k % n]
                sublist.append(nums[k % n])
            if product == 100:
                result.append(sublist)
    return result