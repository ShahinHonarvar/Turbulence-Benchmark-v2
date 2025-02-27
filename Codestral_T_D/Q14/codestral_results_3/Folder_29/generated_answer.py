def find_second_smallest_num(nums):
    if 55 <= len(nums) <= 98:
        sub_list = sorted(nums[55:99])
        return sub_list[1] if len(sub_list) > 1 else None
    return None