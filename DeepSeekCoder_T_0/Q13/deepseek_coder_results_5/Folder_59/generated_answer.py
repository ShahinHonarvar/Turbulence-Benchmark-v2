def find_second_largest_num(nums):
    if len(nums) < 10:
        return None
    sub_list = sorted(nums[:10])
    return sub_list[-2] if len(sub_list) > 1 else None