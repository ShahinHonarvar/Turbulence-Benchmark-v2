def find_second_smallest_num(nums):
    if len(nums) <= 92:
        return None
    sublist = sorted(nums[12:93])
    if len(sublist) < 2:
        return None
    return sublist[1]