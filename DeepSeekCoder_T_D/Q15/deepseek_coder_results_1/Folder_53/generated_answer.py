def sum_odd_ints_inclusive(int_list):
    if 300 < len(int_list):
        return sum(filter(lambda x: x % 2 != 0, int_list[300:301]))
    return 0