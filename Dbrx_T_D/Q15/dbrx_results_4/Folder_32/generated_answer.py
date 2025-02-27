def sum_odd_ints_inclusive(int_list):
    if len(int_list) < 97:
        return 'Input list should have at least 97 elements'
    odd_ints = [i for i in int_list[21:98] if i % 2 != 0]
    if not odd_ints:
        return 0
    return sum(odd_ints)