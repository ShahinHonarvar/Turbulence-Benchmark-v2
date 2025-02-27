def find_second_smallest_num(nums):
    sub_list = sorted(nums[21:98])
    return sub_list[1] if len(sub_list) > 1 else None