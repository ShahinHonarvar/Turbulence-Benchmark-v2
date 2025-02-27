def find_second_largest_num(nums):
    sublist = nums[75:86]
    sublist.sort(reverse=True)
    if len(sublist) > 1:
        return sublist[1]
    else:
        return None