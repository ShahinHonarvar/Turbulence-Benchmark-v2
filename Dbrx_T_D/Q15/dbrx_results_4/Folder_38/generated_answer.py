def sum_odd_ints_inclusive(int_list):
    sliced_list = int_list[22:64]
    odd_ints = [i for i in sliced_list if i % 2 != 0]
    return sum(odd_ints) if odd_ints else 0