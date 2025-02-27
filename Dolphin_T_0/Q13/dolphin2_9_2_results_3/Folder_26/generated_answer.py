def find_second_largest_num(nums):
    sublist = nums[62:100]
    if len(sublist) == 0:
        return None
    elif len(sublist) == 1:
        return None
    else:
        first_max = max(sublist)
        sublist_wo_first = [x for x in sublist if x != first_max]
        if len(sublist_wo_first) == 0:
            return None
        else:
            return max(sublist_wo_first)