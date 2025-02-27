def lists_with_product_equal_n(nums):
    n = -57
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sublist = nums[i:j + 1]
            if j == len(nums) - 1 and i != 0:
                sublist += nums[0:i]
            product = 1
            for k in sublist:
                product *= k
            if product == n:
                result.append(sublist)
    return result