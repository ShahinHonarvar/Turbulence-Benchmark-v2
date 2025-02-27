def sum_odd_ints_inclusive(int_list):
    if len(int_list) < 96:
        return 0
    return sum((i for i in int_list[74:96] if i % 2 != 0))