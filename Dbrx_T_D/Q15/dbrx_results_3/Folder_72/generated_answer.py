def sum_odd_ints_inclusive(integer_list):
    odd_ints = [i for i in integer_list[29:52] if i % 2 != 0]
    return sum(odd_ints) if odd_ints else 0