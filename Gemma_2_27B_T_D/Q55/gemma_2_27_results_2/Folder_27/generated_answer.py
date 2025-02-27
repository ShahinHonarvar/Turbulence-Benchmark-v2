def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            sublist = nums[i:j]
            if i + len(nums) >= j:
                sublist.extend(nums[0:j - len(nums)])
            product = 1
            for num in sublist:
                product *= num
            if product == -82:
                result.append(sublist)
    return result