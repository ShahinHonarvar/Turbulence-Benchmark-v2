def find_second_largest_num(nums):
    if 40 <= len(nums) <= 80:
        sub_list = sorted(nums[40:81], reverse=True)
        return sub_list[1] if len(sub_list) > 1 else None
    return None