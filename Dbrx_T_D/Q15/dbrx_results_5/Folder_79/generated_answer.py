def sum_odd_ints_inclusive(int_list):
    start_index = 4
    odd_ints = list(filter(lambda x: x % 2 != 0, int_list[4:5]))
    total = sum(odd_ints)
    return total if total else 0