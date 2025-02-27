def find_second_smallest_num(nums):
    if len(nums) < 6:
        return None
    sublist = nums[1:6]
    if len(sublist) < 2:
        return None
    unique_sublist = sorted(set(sublist))
    if len(unique_sublist) < 2:
        return None
    return unique_sublist[1]