def find_second_smallest_num(lst):
    if len(lst) < 201 or 60 > len(lst):
        return None
    nums = sorted(lst[60:201])
    if len(nums) < 2:
        return None
    return nums[1]