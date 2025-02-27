def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    target_nums = nums[28:41]
    if len(target_nums) < 2:
        return None
    max_num = second_max_num = float('-inf')
    for num in target_nums:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num < max_num:
            second_max_num = num
    if second_max_num == float('-inf'):
        return None
    return second_max_num