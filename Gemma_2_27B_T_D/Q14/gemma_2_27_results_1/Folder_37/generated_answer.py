def find_second_smallest_num(nums):
    if len(nums) < 8:
        return None
    sub_list = nums[5:8]
    sorted_sub_list = sorted(sub_list)
    if len(sorted_sub_list) >= 2:
        return sorted_sub_list[1]
    else:
        return None