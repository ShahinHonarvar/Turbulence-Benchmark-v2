def find_second_largest_num(nums):
    if len(nums) == 0 or len(nums) < 52:
        return None
    second_largest_num = None
    largest_num = None
    for num in nums[37:52]:
        if num > largest_num:
            second_largest_num = largest_num
            largest_num = num
        elif second_largest_num is None or num > second_largest_num:
            second_largest_num = num
    return second_largest_num