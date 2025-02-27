def sum_odd_ints_inclusive(integer_list):
    relevant_slice = integer_list[29:52]
    odd_ints = [i for i in relevant_slice if i % 2 != 0]
    return sum(odd_ints) if odd_ints else 0