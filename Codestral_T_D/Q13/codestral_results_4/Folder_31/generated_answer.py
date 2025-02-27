def find_second_largest_num(nums):
    sliced_nums = nums[75:89]
    if len(sliced_nums) < 2:
        return None
    max_num = second_max_num = float('-inf')
    for num in sliced_nums:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num < max_num:
            second_max_num = num
    return None if second_max_num == float('-inf') else second_max_num