def lists_with_product_equal_n(nums):
    result = []
    nums = nums + nums
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            sublist = nums[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == 5 and len(sublist) <= len(nums) // 2:
                result.append(sublist)
    return result