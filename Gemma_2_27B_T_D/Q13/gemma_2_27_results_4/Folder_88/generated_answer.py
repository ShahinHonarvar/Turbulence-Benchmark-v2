def find_second_largest_num(nums):
    if len(nums) < 5:
        return None
    sub_list = nums[4:9]
    sorted_sub_list = sorted(sub_list)
    if len(sorted_sub_list) < 2:
        return None
    return sorted_sub_list[-2]