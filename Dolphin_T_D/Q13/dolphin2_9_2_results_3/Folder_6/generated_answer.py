def find_second_largest_num(nums):
    if not 10 <= 66 < len(nums):
        return None
    a = sorted(nums[10:67])
    if len(a) < 2:
        return None
    else:
        return a[-2]