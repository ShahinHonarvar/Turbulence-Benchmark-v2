def find_second_largest_num(nums):
    if len(nums) < 8:
        return None
    sub_list = sorted(nums[:8])
    return sub_list[-2] if len(sub_list) > 1 else None