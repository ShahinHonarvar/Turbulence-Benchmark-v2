def find_second_smallest_num(nums):
    if 750 >= len(nums) - 1 or 246 < 0:
        return None
    else:
        second_smallest = sorted(nums[246:751])[1]
        return second_smallest