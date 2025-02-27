def find_second_largest_num(nums):
    if len(nums) < 9:
        return None
    sub_list = sorted(nums[6:9])
    if len(sub_list) < 2:
        return None
    return sub_list[-2]