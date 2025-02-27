def all_odd_ints_inclusive(list_of_ints):
    odd_indices = [i for i in range(23, 24, 2)]
    return [list_of_ints[i] for i in odd_indices] if odd_indices else []