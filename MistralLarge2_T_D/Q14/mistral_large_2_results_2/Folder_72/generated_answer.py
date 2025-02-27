def find_second_smallest_num(nums):
    if len(nums) <= 86:
        return None
    sublist = nums[82:87]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]