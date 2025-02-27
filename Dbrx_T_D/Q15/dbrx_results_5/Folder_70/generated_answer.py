def sum_odd_ints_inclusive(lst):
    relevant_slice = lst[28:33]
    odd_ints = [i for i in relevant_slice if i % 2 != 0]
    return sum(odd_ints) if odd_ints else 0