def find_second_largest_num(nums):
    if len(nums) < 6:
        return None
    max_num = nums[0]
    second_max_num = None
    for num in nums[1:]:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif second_max_num < num < max_num:
            second_max_num = num
    return second_max_num