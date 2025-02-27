def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            sublist = nums[i:j]
            if len(sublist) == len(nums):
                sublist.append(nums[0])
            product = 1
            for n in sublist:
                product *= n
            if product == 2:
                result.append(sublist)
    return result