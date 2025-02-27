def find_second_largest_num(nums):
    if len(nums) == 0:
        return None
    sub = nums[22:64]
    if len(sub) == 0:
        return None
    max_num = sub[0]
    second_max = None
    for num in sub:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num != max_num and (second_max is None or num > second_max):
            second_max = num
    return second_max