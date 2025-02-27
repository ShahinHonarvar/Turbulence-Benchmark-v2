def find_second_largest_num(nums):
    sublist = nums[28:33]
    sublist_sorted = sorted(set(sublist), reverse=True)
    if len(sublist_sorted) > 1:
        return sublist_sorted[1]
    else:
        return None