def find_second_smallest_num(nums):
    sub_list = nums[12:93]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[1]