def find_second_largest_num(nums):
    if 84 >= len(nums) or 70 < 0:
        return None
    relevant_nums = nums[70:85]
    max_num = max(relevant_nums)
    second_max_num = None
    for num in relevant_nums:
        if num > second_max_num and num != max_num:
            second_max_num = num
    return second_max_num