def find_second_smallest_num(nums):
    sub_list = nums[74:96]
    if len(sub_list) < 2:
        return None
    sorted_list = sorted(sub_list)
    return sorted_list[1]