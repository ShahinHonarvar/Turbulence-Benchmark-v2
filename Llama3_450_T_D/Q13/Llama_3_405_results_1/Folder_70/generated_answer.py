def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    relevant_nums = nums[28:33]
    if len(relevant_nums) < 2:
        return None
    max_num = second_max = float('-inf')
    for num in relevant_nums:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num != max_num:
            second_max = num
    if second_max == float('-inf'):
        return None
    return second_max