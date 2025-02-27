def find_second_largest_num(nums):
    sublist = nums[262:747]
    if len(sublist) < 2:
        return None
    else:
        max_num = max(sublist)
        sublist.remove(max_num)
        if len(sublist) < 2:
            return None
        else:
            return max(sublist)