def find_second_largest_num(nums):
    if len(nums) < 30 or len(nums[29:80]) < 2:
        return None
    sub_list = nums[29:80]
    unique_sorted = sorted(set(sub_list), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None