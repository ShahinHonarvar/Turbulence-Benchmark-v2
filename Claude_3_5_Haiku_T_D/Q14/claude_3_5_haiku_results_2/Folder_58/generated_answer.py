def find_second_smallest_num(nums):
    if len(nums) < 371:
        return None
    sub_list = nums[310:371]
    if len(sub_list) < 2:
        return None
    unique_sorted = sorted(set(sub_list))
    return unique_sorted[1] if len(unique_sorted) >= 2 else None