def find_second_largest_num(nums):
    sub_list = nums[30:88]
    sub_list.sort()
    return sub_list[-2] if len(sub_list) > 1 else None