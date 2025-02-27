def find_second_smallest_num(nums):
    if len(nums) < 50:
        return None
    sublist = nums[22:51]
    sublist_sorted = sorted(sublist)
    if len(sublist_sorted) < 2:
        return None
    return sublist_sorted[1]