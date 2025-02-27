def find_second_smallest_num(nums):
    nums_sorted = sorted(nums[246:751])
    if len(nums_sorted) < 2:
        return None
    return nums_sorted[1]