def find_second_largest_num(nums):
    if len(nums) < 88:
        return None
    sublist = nums[30:88]
    if len(sublist) < 2:
        return None
    sublist.sort(reverse=True)
    return sublist[1]