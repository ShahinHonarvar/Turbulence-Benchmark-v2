def find_second_largest_num(nums):
    sublist = nums[32:36]
    sublist.sort(reverse=True)
    if len(sublist) < 2:
        return None
    else:
        return sublist[1]