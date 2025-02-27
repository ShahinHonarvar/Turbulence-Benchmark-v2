def find_second_smallest_num(nums):
    if 98 < len(nums) < 55:
        return None
    sublist = nums[55:99]
    unique_sorted_sublist = sorted(list(set(sublist)))
    if len(unique_sorted_sublist) < 2:
        return None
    return unique_sorted_sublist[1]