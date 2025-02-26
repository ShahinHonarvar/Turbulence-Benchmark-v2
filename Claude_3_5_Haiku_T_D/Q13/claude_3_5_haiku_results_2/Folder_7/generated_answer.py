def find_second_largest_num(nums):
    if len(nums) < 662:
        return None
    sub_list = nums[661:925]
    if len(sub_list) == 0:
        return None
    sorted_sub_list = sorted(set(sub_list), reverse=True)
    return sorted_sub_list[1] if len(sorted_sub_list) > 1 else None