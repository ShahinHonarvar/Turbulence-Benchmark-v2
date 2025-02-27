def sum_ints_div_by_either_nums(int_list):
    if len(int_list) < 82:
        return 0
    return sum((n for n in int_list[78:82] if n % 76 == 0 or n % 60 == 0))