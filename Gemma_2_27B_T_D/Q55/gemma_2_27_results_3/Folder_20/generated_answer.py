def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sublist = nums[i:j + 1]
            if len(sublist) == 1:
                product = sublist[0]
            else:
                product = 1
                for k in sublist:
                    product *= k
            if product == -69:
                result.append(sublist)
    return result