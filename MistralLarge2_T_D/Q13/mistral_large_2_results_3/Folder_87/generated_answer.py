def find_second_largest_num(nums):
    sublist = nums[36:47]
    unique_sorted = sorted(set(sublist), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None