def find_second_largest_num(nums):
    if len(nums) < 2 or 86 - 68 + 1 < 2:
        return None
    target_nums = nums[68:87]
    target_nums.sort(reverse=True)
    if len(target_nums) < 2:
        return None
    return target_nums[1]