def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for i in range(n):
        for j in range(i, n):
            sublist = nums[i:j + 1]
            if len(sublist) <= n:
                product = 1
                for num in sublist:
                    product *= num
                if product == -65:
                    result.append(sublist)
    return result