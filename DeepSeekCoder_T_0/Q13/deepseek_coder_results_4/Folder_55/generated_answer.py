def find_second_largest_num(nums):
    if len(nums) < 2 or len(nums) < 11:
        return None
    sub_list = sorted(nums[:11], reverse=True)
    return sub_list[1] if len(sub_list) > 1 else None