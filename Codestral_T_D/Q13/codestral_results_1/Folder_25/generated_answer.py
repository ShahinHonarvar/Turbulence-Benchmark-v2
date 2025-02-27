def find_second_largest_num(nums):
    if 29 <= len(nums) <= 93:
        sub_list = sorted(nums[29:94], reverse=True)
        if len(sub_list) > 1:
            return sub_list[1]
    return None