def sum_ints_div_by_either_nums(int_list):
    if len(int_list) < 87:
        return 0
    sub_list = int_list[73:87]
    return sum((x for x in sub_list if x % 54 == 0 or x % 82 == 0))