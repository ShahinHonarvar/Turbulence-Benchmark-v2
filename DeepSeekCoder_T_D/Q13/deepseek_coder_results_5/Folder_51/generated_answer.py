def find_second_largest_num(nums):
    if len(nums) < 9:
        return None
    sub_list = sorted(nums[1:9])
    return sub_list[-2] if len(sub_list) > 1 else None