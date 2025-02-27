def find_second_smallest_num(lst):
    if len(lst) < 73:
        return None
    nums = sorted(lst[31:73])
    return nums[1] if len(nums) > 1 else None