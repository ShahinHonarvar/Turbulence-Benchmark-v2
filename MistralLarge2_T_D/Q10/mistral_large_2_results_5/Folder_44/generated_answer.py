def all_odd_ints_exclusive(int_list):
    return [num for idx, num in enumerate(int_list) if 81 < idx < 86 and num % 2 != 0]