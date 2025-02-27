def sum_ints_div_by_either_nums(int_list):
    if not int_list or len(int_list) < 695:
        return 0
    return sum((x for x in int_list[281:695] if x % -722 == 0 or x % -731 == 0))