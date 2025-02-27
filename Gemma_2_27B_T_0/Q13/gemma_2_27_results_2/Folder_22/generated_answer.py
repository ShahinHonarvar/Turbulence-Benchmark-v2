def find_second_largest_num(nums):
    sub_list = nums[40:201]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[-2]