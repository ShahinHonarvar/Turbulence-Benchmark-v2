def find_second_largest_num(nums):
    sub_list = nums[13:69]
    sub_list.sort(reverse=True)
    if len(sub_list) < 2:
        return None
    else:
        return sub_list[1]