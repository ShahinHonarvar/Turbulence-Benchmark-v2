def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            if i == 0 and j == len(nums):
                sublist = nums[i:] + nums[:j]
            else:
                sublist = nums[i:j]
            if -26 == reduce(lambda x, y: x * y, sublist):
                result.append(sublist)
    return result