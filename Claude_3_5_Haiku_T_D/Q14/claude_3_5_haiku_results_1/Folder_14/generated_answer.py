def find_second_smallest_num(nums):
    if len(nums) < 10:
        return None
    selected_range = nums[8:10]
    if len(selected_range) < 2:
        return None
    sorted_range = sorted(set(selected_range))
    return sorted_range[1] if len(sorted_range) >= 2 else None