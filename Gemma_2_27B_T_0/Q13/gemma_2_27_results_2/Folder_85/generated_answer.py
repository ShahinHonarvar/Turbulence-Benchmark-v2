def find_second_largest_num(nums):
    if len(nums) < 9:
        return None
    sub_list = nums[6:9]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[-2]