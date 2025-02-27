def find_second_smallest_num(nums):
    if 59 < len(nums) < 25:
        return None
    sublist = nums[25:60]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]