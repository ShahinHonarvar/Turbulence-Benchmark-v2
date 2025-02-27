def sum_odd_ints_inclusive(nested_list):
    odd_ints = [i for i in nested_list[29:94] if i % 2 != 0]
    return sum(odd_ints) if odd_ints else 0