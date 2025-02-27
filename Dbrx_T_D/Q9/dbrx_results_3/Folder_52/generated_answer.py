def all_odd_ints_inclusive(int_list):
    odd_indices = list(range(28, 39))
    odd_ints = [int_list[i] for i in odd_indices if int_list[i] % 2 != 0]
    return odd_ints