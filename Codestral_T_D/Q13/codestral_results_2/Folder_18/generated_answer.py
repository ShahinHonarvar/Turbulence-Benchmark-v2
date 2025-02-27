def find_second_largest_num(nums):
    if 35 <= len(nums) <= 49:
        sub_list = sorted(nums[35:50], reverse=True)
        return sub_list[1] if len(sub_list) > 1 else None
    return None