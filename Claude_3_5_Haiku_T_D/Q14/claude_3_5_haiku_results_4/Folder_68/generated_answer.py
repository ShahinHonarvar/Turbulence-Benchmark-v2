def find_second_smallest_num(nums):
    if len(nums) < 2 or len(nums) < 9:
        return None
    sub_list = nums[:9]
    sorted_sub_list = sorted(set(sub_list))
    return sorted_sub_list[1] if len(sorted_sub_list) >= 2 else None