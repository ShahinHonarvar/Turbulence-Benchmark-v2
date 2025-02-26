def find_second_smallest_num(nums):
    if len(nums) < 50:
        return None
    sub_list = nums[35:50]
    if len(sub_list) < 2:
        return None
    sorted_sub_list = sorted(set(sub_list))
    return sorted_sub_list[1] if len(sorted_sub_list) >= 2 else None