def sum_ints_div_by_either_nums(lst):
    if not 69 <= len(lst) <= 97:
        return 0
    else:
        sub_list = lst[69:98]
        return sum((x for x in sub_list if x % -90 == 0 or x % -67 == 0))