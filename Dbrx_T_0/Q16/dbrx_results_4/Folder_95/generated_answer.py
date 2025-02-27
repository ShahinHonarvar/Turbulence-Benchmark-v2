def sum_even_ints_inclusive(int_list):
    if len(int_list) < 87:
        return 0
    else:
        return sum((x for x in int_list[82:87] if x % 2 == 0))