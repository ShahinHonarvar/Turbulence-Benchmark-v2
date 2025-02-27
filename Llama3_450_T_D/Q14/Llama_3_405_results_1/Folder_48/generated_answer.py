def find_second_smallest_num(nums):
    if len(nums) < 2 or 750 >= len(nums) or 246 < 0:
        return None
    else:
        return sorted(nums[246:751])[1]