def find_second_largest_num(nums):
    sliced_nums = nums[6:9]
    if len(sliced_nums) < 2:
        return None
    max_num = second_max = float('-inf')
    for num in sliced_nums:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num < max_num:
            second_max = num
    if second_max == float('-inf'):
        return None
    return second_max