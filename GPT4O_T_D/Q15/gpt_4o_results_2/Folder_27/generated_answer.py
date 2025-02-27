def sum_odd_ints_inclusive(int_list):
    if len(int_list) < 94:
        return 0
    return sum((i for i in int_list[66:94] if i % 2 != 0))