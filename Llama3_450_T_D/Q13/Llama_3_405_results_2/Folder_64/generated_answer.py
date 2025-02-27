def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    max_num = second_max_num = float('-inf')
    for i in range(min(5, len(nums))):
        if nums[i] > max_num:
            second_max_num = max_num
            max_num = nums[i]
        elif nums[i] > second_max_num and nums[i] != max_num:
            second_max_num = nums[i]
    if second_max_num == float('-inf'):
        return None
    return second_max_num