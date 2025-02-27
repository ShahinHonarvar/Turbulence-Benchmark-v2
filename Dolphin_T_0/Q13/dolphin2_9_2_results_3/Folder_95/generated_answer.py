def find_second_largest_num(lst):
    sub_list = lst[82:87] if len(lst) > 86 else lst
    unique_nums = list(set(sub_list))
    if len(unique_nums) < 2:
        return None
    else:
        unique_nums.sort()
        return unique_nums[-2]