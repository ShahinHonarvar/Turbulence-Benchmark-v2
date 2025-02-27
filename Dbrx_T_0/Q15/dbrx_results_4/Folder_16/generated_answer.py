def sum_odd_ints_inclusive(int_list):
    odd_ints = [i for i in int_list[33:37] if i % 2 != 0]
    return sum(odd_ints) if odd_ints else 0