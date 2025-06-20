def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    nums = nums[74:96]
    if len(nums) < 2:
        return None
    max_num = second_max = float('-inf')
    for num in nums:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num != max_num:
            second_max = num
    if second_max == float('-inf'):
        return None
    return second_max