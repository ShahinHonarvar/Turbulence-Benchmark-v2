def sum_odd_ints_inclusive(integer_list):
    odd_integers = [i for i in integer_list[81:87] if i % 2 != 0]
    return sum(odd_integers) if len(odd_integers) > 0 else 0