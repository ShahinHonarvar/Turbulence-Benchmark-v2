def find_second_largest_num(nums):
    if len(nums) == 0:
        return None
    max_num = float('-inf')
    second_max_num = float('-inf')
    for i in range(43, 52):
        if nums[i] > max_num:
            second_max_num = max_num
            max_num = nums[i]
        elif nums[i] > second_max_num:
            second_max_num = nums[i]
    if second_max_num == float('-inf'):
        return None
    else:
        return second_max_num