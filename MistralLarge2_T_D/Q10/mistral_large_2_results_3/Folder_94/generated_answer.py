def all_odd_ints_exclusive(int_list):
    return [num for idx, num in enumerate(int_list) if 28 < idx < 53 and num % 2 != 0]