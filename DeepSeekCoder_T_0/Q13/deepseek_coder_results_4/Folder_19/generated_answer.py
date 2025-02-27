def find_second_largest_num(nums):
    sublist = nums[3:6]
    if len(sublist) < 3:
        return None
    sublist.sort()
    return sublist[1]