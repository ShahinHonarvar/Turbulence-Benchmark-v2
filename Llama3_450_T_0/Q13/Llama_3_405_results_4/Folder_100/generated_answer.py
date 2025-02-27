def find_second_largest_num(nums):
    if len(nums) < 69:
        return None
    sliced_nums = nums[42:69]
    if len(sliced_nums) < 2:
        return None
    max_num = second_max_num = float('-inf')
    for num in sliced_nums:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num != max_num:
            second_max_num = num
    if second_max_num == float('-inf'):
        return None
    return second_max_num