def find_second_smallest_num(nums):
    if len(nums) < 14:
        return None
    sub_list = nums[13:69]
    if len(sub_list) == 0:
        return None
    sorted_sub_list = sorted(set(sub_list))
    return sorted_sub_list[1] if len(sorted_sub_list) > 1 else None