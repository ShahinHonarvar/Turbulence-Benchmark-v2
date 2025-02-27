def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    max_num = second_max = float('-inf')
    for i in range(min(9, len(nums))):
        if nums[i] > max_num:
            second_max = max_num
            max_num = nums[i]
        elif nums[i] > second_max and nums[i] != max_num:
            second_max = nums[i]
    if second_max == float('-inf'):
        return None
    return second_max