def find_second_largest_num(nums):
    sub_list = nums[40:81]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    else:
        return sub_list[-2]