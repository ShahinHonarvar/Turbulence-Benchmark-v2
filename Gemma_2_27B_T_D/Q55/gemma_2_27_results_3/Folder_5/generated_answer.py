def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            sublist = nums[i:j]
            if len(sublist) > 0 and (j == len(nums) and i > 0 or j < len(nums)):
                sublist.extend(nums[:i])
            product = 1
            for num in sublist:
                product *= num
            if product == -33:
                result.append(sublist)
    return result