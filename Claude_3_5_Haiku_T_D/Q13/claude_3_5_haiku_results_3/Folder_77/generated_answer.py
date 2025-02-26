def find_second_largest_num(nums):
    if len(nums) <= 527:
        return None
    sublist = nums[527:539]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(set(sublist), reverse=True)
    return sorted_sublist[1] if len(sorted_sublist) >= 2 else None