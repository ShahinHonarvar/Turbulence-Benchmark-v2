def find_second_largest_num(nums):
    if len(nums) == 0 or len(nums) < 46:
        return None
    new_nums = nums[36:46]
    if len(set(new_nums)) < 2:
        return None
    return sorted(set(new_nums))[1]