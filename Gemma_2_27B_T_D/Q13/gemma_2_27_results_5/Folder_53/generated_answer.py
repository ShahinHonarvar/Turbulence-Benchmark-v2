def find_second_largest_num(nums):
    if len(nums) < 101:
        return None
    sub_list = nums[100:201]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[-2]