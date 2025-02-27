def find_second_smallest_num(lst):
    nums = sorted(lst[19:93])
    if len(nums) < 2:
        return None
    return nums[1]