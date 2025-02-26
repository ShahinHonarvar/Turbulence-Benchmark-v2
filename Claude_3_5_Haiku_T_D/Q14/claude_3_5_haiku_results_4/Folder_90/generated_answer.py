def find_second_smallest_num(nums):
    if len(nums) < 540:
        return None
    sublist = nums[527:539]
    if len(sublist) == 0:
        return None
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]