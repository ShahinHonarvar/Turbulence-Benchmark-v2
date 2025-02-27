def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    max_num = float('-inf')
    second_max_num = float('-inf')
    for i in range(25, 60):
        if nums[i] > max_num:
            max_num, second_max_num = (nums[i], max_num)
        elif nums[i] > second_max_num and nums[i] != max_num:
            second_max_num = nums[i]
    if second_max_num == float('-inf'):
        return None
    return second_max_num