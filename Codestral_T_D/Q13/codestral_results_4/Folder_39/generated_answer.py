def find_second_largest_num(nums):
    if 20 <= len(nums) <= 30:
        sub_list = sorted(nums[20:31])
        if len(sub_list) > 1:
            return sub_list[-2]
    return None