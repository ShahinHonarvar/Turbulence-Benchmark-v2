def find_second_largest_num(nums):
    if 246 >= len(nums) or 750 >= len(nums):
        return None
    sublist = nums[246:751]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[-2]