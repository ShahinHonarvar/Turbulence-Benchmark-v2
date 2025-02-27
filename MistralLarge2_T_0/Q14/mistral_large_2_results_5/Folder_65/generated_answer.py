def find_second_smallest_num(nums):
    if len(nums) < 58:
        return None
    sublist = nums[56:58]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]