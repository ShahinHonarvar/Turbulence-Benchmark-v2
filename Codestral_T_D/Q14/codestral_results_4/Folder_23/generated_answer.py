def find_second_smallest_num(nums):
    sub_list = sorted(nums[19:93])
    if len(sub_list) < 2:
        return None
    else:
        return sub_list[1]