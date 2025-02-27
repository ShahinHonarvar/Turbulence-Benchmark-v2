def sum_odd_ints_inclusive(int_list):
    if 25 <= len(int_list) - 1 < 87:
        return sum((x for x in int_list[25:88] if x % 2 != 0))
    elif len(int_list) - 1 >= 87:
        return sum((x for x in int_list[25:88] if x % 2 != 0))
    else:
        return 0