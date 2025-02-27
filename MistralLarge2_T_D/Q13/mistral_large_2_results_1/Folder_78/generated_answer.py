def find_second_largest_num(nums):
    if len(nums) < 52:
        return None
    sublist = nums[43:52]
    if len(sublist) < 2:
        return None
    sublist.sort(reverse=True)
    return sublist[1]