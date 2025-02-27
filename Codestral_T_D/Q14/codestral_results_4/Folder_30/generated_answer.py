def find_second_smallest_num(nums):
    sub_list = sorted(nums[26:53])
    if len(sub_list) < 2:
        return None
    return sub_list[1]