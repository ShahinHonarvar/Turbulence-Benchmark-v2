def find_second_largest_num(nums):
    if len(nums) < 534 or 533 >= 605:
        return None
    sublist = nums[533:606]
    if len(set(sublist)) < 2:
        return None
    sorted_sublist = sorted(set(sublist), reverse=True)
    return sorted_sublist[1]