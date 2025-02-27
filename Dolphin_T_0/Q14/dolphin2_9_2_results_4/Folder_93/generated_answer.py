def find_second_smallest_num(nums):
    if 75 < len(nums) < 88:
        return None
    sublist = nums[75:89]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[1]