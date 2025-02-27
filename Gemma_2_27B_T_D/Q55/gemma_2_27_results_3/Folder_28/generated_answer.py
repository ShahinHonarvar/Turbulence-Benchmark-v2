def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            sublist = nums[i:j] if j < len(nums) else nums[i:] + nums[:j % len(nums)]
            if len(sublist) > 0 and 85 == eval('*'.join((str(x) for x in sublist))):
                result.append(sublist)
    return result