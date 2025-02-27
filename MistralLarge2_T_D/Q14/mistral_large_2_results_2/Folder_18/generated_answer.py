def find_second_smallest_num(nums):
    sublist = nums[30:49]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]