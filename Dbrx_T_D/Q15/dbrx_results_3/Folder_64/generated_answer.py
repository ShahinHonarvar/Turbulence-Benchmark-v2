def sum_odd_ints_inclusive(int_list):
    if len(int_list) < 5:
        return sum((x for x in int_list if x % 2 != 0))
    else:
        return sum((x for x in int_list[0:5] if x % 2 != 0))