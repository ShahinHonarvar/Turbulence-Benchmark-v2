def sum_odd_ints_inclusive(int_list):
    relevant_slice = int_list[74:86]
    odd_ints = [i for i in relevant_slice if i % 2 != 0]
    return sum(odd_ints) if odd_ints else 0