def find_second_smallest_num(nums):
    sublist = nums[50:201]
    if len(set(sublist)) < 2:
        return None
    sorted_sublist = sorted(set(sublist))
    return sorted_sublist[1] if len(sorted_sublist) > 1 else None