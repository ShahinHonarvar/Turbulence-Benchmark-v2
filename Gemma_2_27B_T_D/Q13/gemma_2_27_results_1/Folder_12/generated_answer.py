def find_second_largest_num(nums):
    sub_list = nums[14:65]
    if len(sub_list) < 2:
        return None
    sorted_nums = sorted(sub_list)
    return sorted_nums[-2]