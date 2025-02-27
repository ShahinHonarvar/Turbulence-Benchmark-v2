def find_second_largest_num(lst):
    sub_lst = lst[30:88]
    if len(sub_lst) < 2:
        return None
    unique_nums = set(sub_lst)
    if len(unique_nums) < 2:
        return None
    sorted_nums = sorted(unique_nums, reverse=True)
    return sorted_nums[1]