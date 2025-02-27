def find_second_largest_num(nums):
    sub_list = nums[10:67]
    if len(sub_list) < 2:
        return None
    else:
        sub_list.sort(reverse=True)
        return sub_list[1]