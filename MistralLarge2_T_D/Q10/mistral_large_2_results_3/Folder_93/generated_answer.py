def all_odd_ints_exclusive(int_list):
    return [num for idx, num in enumerate(int_list) if 19 < idx < 94 and num % 2 != 0]