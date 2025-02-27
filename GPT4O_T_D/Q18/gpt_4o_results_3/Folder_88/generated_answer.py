def sum_ints_div_by_either_nums(lst):
    if len(lst) < 4:
        return 0
    sub_list = lst[3:10]
    total_sum = sum((x for x in sub_list if x % 6 == 0 or x % 1 == 0))
    return total_sum