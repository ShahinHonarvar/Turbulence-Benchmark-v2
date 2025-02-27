def find_second_smallest_num(lst):
    if len(lst) < 201:
        return None
    nums = sorted(set(lst[50:201]))
    if len(nums) < 2:
        return None
    return nums[1]