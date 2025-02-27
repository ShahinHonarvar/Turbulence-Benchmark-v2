def find_second_smallest_num(nums):
    if not 37 <= len(nums) >= 76:
        return None
    else:
        sub_list = sorted(nums[37:77])
        return sub_list[1] if len(sub_list) > 1 else None