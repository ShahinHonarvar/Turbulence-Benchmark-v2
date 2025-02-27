def sum_odd_ints_inclusive(int_list):
    if len(int_list) < 9:
        check_range = int_list
    else:
        check_range = int_list[:9]
    return sum((x for x in check_range if x % 2 != 0))