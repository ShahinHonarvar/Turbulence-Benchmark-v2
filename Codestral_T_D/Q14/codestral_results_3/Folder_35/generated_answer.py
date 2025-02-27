def find_second_smallest_num(nums):
    if len(nums) < 40:
        return None
    sublist = nums[15:40]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[1]