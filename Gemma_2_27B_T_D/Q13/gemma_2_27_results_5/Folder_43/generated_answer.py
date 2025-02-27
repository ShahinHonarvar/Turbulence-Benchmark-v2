def find_second_largest_num(nums):
    if 68 >= len(nums) or 86 >= len(nums):
        return None
    sublist = nums[68:87]
    sorted_sublist = sorted(sublist, reverse=True)
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]