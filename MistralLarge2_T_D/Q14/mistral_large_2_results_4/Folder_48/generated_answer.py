def find_second_smallest_num(nums):
    subset = sorted(nums[246:751])
    if len(subset) < 2:
        return None
    return subset[1]