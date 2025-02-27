def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    nums.extend(nums)
    for i in range(n):
        for j in range(i, i + n):
            product = 1
            sublist = []
            for k in range(i, j + 1):
                product *= nums[k]
                sublist.append(nums[k])
                if product == -837:
                    result.append(sublist)
    return result