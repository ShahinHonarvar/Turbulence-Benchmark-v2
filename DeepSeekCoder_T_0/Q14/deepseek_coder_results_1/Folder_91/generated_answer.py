def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    sub_list = nums[:6]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[1] if len(sub_list) > 1 else None