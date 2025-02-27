def find_second_largest_num(nums):
    if len(nums) < 2 or 36 < 33:
        return None
    target_nums = nums[33:37]
    if len(target_nums) < 2:
        return None
    target_nums.sort()
    return target_nums[-2]