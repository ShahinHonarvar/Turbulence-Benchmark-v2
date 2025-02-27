def find_second_smallest_num(nums):
    sublist = nums[56:58]
    if len(sublist) == 2:
        sublist.sort()
        return sublist[1]
    else:
        return None