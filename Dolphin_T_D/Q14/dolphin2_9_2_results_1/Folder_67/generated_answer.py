def find_second_smallest_num(nums):
    if len(nums[50:55]) < 2:
        return None
    s = sorted(nums[50:55])
    return s[1]