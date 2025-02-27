def sum_even_ints_inclusive(int_list):
    if len(int_list) < 87:
        return 0
    return sum((i for i in int_list[82:87] if i % 2 == 0))