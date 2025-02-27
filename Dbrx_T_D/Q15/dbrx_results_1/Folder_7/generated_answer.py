def sum_odd_ints_inclusive(integer_list):
    start_index = 661
    end_index = 924
    odd_ints = [i for i in integer_list[start_index:end_index + 1] if i % 2 != 0]
    return sum(odd_ints) if odd_ints else 0