def find_second_largest_num(nums):
    sublist = nums[52:72]
    sublist.sort(reverse=True)
    return sublist[1] if len(sublist) > 1 else None