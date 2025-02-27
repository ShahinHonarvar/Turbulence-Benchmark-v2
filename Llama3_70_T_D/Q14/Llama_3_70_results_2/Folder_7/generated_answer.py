def find_second_smallest_num(lst):
    nums = sorted(set(lst[686:988]))
    return nums[1] if len(nums) > 1 else None