def find_second_largest_num(nums):
    if 93 >= len(nums) >= 29:
        sublist = nums[29:94]
        sublist.sort(reverse=True)
        if len(sublist) > 1:
            return sublist[1]
    return None