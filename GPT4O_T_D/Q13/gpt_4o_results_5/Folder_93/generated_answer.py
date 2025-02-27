def find_second_largest_num(nums):
    if len(nums) < 95:
        return None
    sub_list = nums[75:95]
    if len(sub_list) < 2:
        return None
    unique_sorted_list = sorted(set(sub_list), reverse=True)
    return unique_sorted_list[1] if len(unique_sorted_list) > 1 else None