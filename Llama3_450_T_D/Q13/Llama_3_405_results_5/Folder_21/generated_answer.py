def find_second_largest_num(nums):
    if len(nums) < 2 or 639 >= len(nums) or 975 < 0:
        return None
    start = max(0, 639)
    end = min(len(nums), 976)
    target_nums = nums[start:end]
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