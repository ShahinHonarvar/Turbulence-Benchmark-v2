def find_second_smallest_num(list_nums):
    sub_list = sorted(list_nums[31:73])
    if len(sub_list) < 2:
        return None
    return sub_list[1]