def find_second_smallest_num(nums):
    if len(nums) < 557:
        return None
    sublist = nums[209:557]
    if len(sublist) < 2:
        return None
    unique_sorted = sorted(set(sublist))
    if len(unique_sorted) < 2:
        return None
    return unique_sorted[1]