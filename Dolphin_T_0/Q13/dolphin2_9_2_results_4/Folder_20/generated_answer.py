def find_second_largest_num(nums):
    if 66 >= len(nums) or 56 < 0:
        return None
    sublist = nums[56:67]
    if len(sublist) < 2:
        return None
    else:
        sorted_sublist = sorted(sublist, reverse=True)
        return sorted_sublist[1]