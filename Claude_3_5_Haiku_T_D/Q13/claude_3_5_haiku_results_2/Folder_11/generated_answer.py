def find_second_largest_num(nums):
    if len(nums) <= 51:
        return None
    sub_list = nums[37:52]
    if len(sub_list) == 0:
        return None
    unique_sub_list = sorted(set(sub_list), reverse=True)
    return unique_sub_list[1] if len(unique_sub_list) > 1 else None