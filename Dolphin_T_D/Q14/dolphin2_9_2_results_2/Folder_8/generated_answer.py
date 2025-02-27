def find_second_smallest_num(nums):
    sublist = nums[56:67]
    if len(sublist) < 2:
        return None
    else:
        sublist.sort()
        return sublist[1]