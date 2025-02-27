def sum_ints_div_by_either_nums(int_list):
    try:
        int_list[7]
    except IndexError:
        return 0
    return sum((i for i in int_list[5:9] if not (i % 5 or i % 7)))