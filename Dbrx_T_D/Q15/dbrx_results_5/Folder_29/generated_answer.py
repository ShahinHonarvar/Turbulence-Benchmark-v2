def sum_odd_ints_inclusive(integer_list):
    sub_list = integer_list[58:98]
    odd_ints = [i for i in sub_list if i % 2 != 0]
    return sum(odd_ints) if odd_ints else 0