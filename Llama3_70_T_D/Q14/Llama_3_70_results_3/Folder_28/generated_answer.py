def find_second_smallest_num(lst):
    nums = sorted(set(lst[22:51]))
    return nums[1] if len(nums) > 1 else None