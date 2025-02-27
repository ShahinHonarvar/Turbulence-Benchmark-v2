def find_second_largest_num(nums):
    sublist = nums[70:85]
    if len(sublist) < 2:
        return None
    else:
        sorted_sublist = sorted(sublist, reverse=True)
        if len(sorted_sublist) == 2:
            return sorted_sublist[1]
        else:
            return None