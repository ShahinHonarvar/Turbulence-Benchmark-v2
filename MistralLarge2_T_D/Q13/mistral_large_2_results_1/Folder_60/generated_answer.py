def find_second_largest_num(nums):
    if len(nums) < 86:
        return None
    sublist = nums[75:86]
    if len(sublist) < 2:
        return None
    sublist.sort(reverse=True)
    return sublist[1]