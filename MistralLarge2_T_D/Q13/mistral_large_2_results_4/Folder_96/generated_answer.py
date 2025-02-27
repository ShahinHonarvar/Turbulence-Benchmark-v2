def find_second_largest_num(nums):
    if len(nums) < 52:
        return None
    sublist = nums[15:52]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist, reverse=True)
    return sorted_sublist[1]