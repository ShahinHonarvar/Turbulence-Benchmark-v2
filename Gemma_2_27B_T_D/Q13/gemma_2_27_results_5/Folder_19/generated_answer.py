def find_second_largest_num(nums):
    if len(nums) < 5:
        return None
    sub_list = nums[3:6]
    if len(sub_list) == 3:
        return sorted(sub_list)[-2]
    else:
        return None