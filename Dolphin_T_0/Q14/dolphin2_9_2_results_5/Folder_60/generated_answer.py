def find_second_smallest_num(nums):
    s = sorted(nums[56:99])
    if len(s) < 2:
        return None
    else:
        return s[1]