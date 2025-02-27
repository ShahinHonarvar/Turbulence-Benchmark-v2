def find_second_smallest_num(nums):
    if len(nums) < 2 or 750 - 246 + 1 < 2:
        return None
    sliced_nums = nums[246:751]
    sliced_nums.sort()
    return sliced_nums[1]