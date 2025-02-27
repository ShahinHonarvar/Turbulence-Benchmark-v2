def find_second_smallest_num(lst):
    if len(lst) < 89:
        return None
    nums = sorted(lst[75:89])
    if len(nums) < 2:
        return None
    return nums[1]