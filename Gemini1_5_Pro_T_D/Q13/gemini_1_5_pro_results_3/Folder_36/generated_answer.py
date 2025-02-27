def find_second_largest_num(nums):
    if len(nums) < 750:
        return None
    sub_nums = nums[246:751]
    if len(set(sub_nums)) < 2:
        return None
    return sorted(sub_nums)[-2]