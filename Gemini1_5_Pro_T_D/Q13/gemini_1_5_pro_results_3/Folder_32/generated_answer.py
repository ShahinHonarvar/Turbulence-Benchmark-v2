def find_second_largest_num(nums):
    if len(nums) < 97:
        return None
    sub_nums = nums[21:98]
    if len(set(sub_nums)) < 2:
        return None
    return sorted(sub_nums)[-2]