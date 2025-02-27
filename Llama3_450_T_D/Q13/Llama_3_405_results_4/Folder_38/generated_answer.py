def find_second_largest_num(nums):
    if len(nums) < 64:
        return None
    slice_nums = nums[22:64]
    if len(slice_nums) < 2:
        return None
    max_num = second_max_num = float('-inf')
    for num in slice_nums:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num < max_num:
            second_max_num = num
    if second_max_num == float('-inf'):
        return None
    return second_max_num