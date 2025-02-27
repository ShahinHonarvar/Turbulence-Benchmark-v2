def find_second_smallest_num(nums):
    if len(nums) <= 6:
        return None
    sublist = sorted(nums[6:7])
    if len(sublist) < 2:
        return None
    return sublist[1]