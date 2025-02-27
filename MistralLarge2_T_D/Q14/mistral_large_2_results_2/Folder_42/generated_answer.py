def find_second_smallest_num(nums):
    if len(nums) < 98:
        return None
    sublist = nums[21:98]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]