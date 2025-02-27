def find_second_largest_num(nums):
    sublist = nums[4:9]
    sublist_sorted = sorted(sublist)
    if len(sublist_sorted) < 2:
        return None
    else:
        return sublist_sorted[-2]