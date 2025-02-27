def find_second_smallest_num(lst):
    if len(lst) < 52:
        return None
    nums = sorted(lst[37:52])
    if len(nums) < 2 or nums[0] == nums[1]:
        return None
    return nums[1]