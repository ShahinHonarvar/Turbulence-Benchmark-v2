def find_second_largest_num(nums):
    sublist = nums[55:99]
    if len(sublist) < 2:
        return None
    else:
        sublist.sort(reverse=True)
        return sublist[1]