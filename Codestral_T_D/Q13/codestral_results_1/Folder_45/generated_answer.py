def find_second_largest_num(nums):
    sub_list = sorted(nums[30:201], reverse=True)
    if len(sub_list) < 2:
        return None
    else:
        return sub_list[1]