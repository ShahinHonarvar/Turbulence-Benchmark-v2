def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for i in range(n):
        for j in range(i, n + i):
            sublist = nums[i:j]
            if len(sublist) > 0 and sublist[-1] == nums[j % n]:
                product = 1
                for num in sublist:
                    product *= num
                if product == -938:
                    result.append(sublist)
    return result