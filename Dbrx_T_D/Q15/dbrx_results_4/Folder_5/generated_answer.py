def sum_odd_ints_inclusive(integer_list):
    start_index = 8
    end_index = 9
    odd_ints = [i for i in integer_list[start_index:end_index + 1] if i % 2 != 0]
    return sum(odd_ints) if odd_ints else 0