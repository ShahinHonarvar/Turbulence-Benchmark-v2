def find_second_smallest_num(nums):
    sub_list = nums[28:39]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[1]