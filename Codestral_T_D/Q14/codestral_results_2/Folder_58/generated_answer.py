def find_second_smallest_num(nums):
    if 310 > len(nums) - 1 or 370 > len(nums) - 1:
        return None
    else:
        sub_list = sorted(nums[310:371])
        return sub_list[1] if len(sub_list) > 1 else None