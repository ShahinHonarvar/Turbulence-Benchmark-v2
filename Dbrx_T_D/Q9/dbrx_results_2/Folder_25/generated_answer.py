def all_odd_ints_inclusive(int_list):
    odd_ints = int_list[29:94]
    odd_ints = [i for i in odd_ints if i % 2 != 0]
    return odd_ints