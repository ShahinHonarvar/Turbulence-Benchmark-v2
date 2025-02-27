def find_second_largest_num(nums):
    if len(nums) == 0:
        return None
    max_num = nums[40]
    second_max_num = None
    for i in range(40, 81):
        if nums[i] > max_num:
            second_max_num = max_num
            max_num = nums[i]
        elif second_max_num is None or (nums[i] > second_max_num and nums[i] < max_num):
            second_max_num = nums[i]
    return second_max_num