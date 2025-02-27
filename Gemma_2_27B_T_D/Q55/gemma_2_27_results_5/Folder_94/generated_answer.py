def lists_with_product_equal_n(nums):
    result = []
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            sublist = nums[i:j + 1]
            if len(sublist) == 1 and sublist[0] == -30:
                result.append(sublist)
            elif len(sublist) > 1:
                product = 1
                for num in sublist:
                    product *= num
                if product == -30:
                    result.append(sublist)
    return result