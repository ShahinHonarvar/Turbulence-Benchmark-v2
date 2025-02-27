def sum_odd_ints_inclusive(int_list):
    if len(int_list) < 97:
        return 'Error: List must have at least 97 elements'
    odd_ints = int_list[20:98]
    return sum((x for x in odd_ints if x % 2 != 0))