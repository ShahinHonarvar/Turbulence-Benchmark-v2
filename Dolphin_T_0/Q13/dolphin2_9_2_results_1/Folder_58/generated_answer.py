def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    max_num = nums[209]
    second_max_num = None
    for num in nums[209:557]:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif second_max_num is None or num > second_max_num:
            second_max_num = num
    return second_max_num