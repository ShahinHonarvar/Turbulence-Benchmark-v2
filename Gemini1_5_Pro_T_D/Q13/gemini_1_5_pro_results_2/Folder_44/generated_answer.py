def find_second_largest_num(nums):
    if len(nums) < 69:
        return None
    sub_nums = nums[13:69]
    if len(set(sub_nums)) < 2:
        return None
    return sorted(sub_nums)[-2]