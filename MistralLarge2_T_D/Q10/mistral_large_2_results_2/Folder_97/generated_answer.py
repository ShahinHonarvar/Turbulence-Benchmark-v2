def all_odd_ints_exclusive(int_list):
    return [num for idx, num in enumerate(int_list) if 20 < idx < 93 and num % 2 != 0]