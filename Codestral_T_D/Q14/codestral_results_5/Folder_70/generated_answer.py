def find_second_smallest_num(nums):
    sub_list = sorted(nums[35:50])
    if len(sub_list) > 1:
        return sub_list[1]
    else:
        return None