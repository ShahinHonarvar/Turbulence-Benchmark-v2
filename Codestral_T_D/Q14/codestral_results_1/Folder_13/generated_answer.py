def find_second_smallest_num(nums):
    sublist = nums[28:33]
    if len(sublist) < 2:
        return None
    else:
        sublist.sort()
        return sublist[1]