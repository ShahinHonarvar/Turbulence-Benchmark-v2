def find_second_largest_num(nums):
    if len(nums) < 15:
        return None
    sub_list = nums[35:50]
    if len(sub_list) < 2:
        return None
    sorted_list = sorted(sub_list)
    return sorted_list[-2]