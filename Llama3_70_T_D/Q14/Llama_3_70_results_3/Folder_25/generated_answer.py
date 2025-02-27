def find_second_smallest_num(lst):
    nums = sorted(lst[37:77])
    if len(nums) < 2:
        return None
    return nums[1]