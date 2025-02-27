def find_second_smallest_num(nums):
    sublist = nums[75:89]
    sublist.sort()
    if len(sublist) < 2:
        return None
    else:
        return sublist[1]