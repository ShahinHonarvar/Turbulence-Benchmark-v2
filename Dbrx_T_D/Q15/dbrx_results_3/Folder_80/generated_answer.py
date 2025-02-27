def sum_odd_ints_inclusive(integer_list):
    relevant_slice = integer_list[63:67]
    odd_ints = [i for i in relevant_slice if i % 2 != 0]
    if odd_ints:
        return sum(odd_ints)
    else:
        return 0