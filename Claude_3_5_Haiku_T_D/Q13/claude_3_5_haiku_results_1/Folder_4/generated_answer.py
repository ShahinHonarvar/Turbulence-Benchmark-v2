def find_second_largest_num(nums):
    if len(nums) < 93:
        return None
    sublist = nums[12:93]
    if len(sublist) < 2:
        return None
    unique_sublist = list(set(sublist))
    if len(unique_sublist) < 2:
        return None
    unique_sublist.sort(reverse=True)
    return unique_sublist[1]