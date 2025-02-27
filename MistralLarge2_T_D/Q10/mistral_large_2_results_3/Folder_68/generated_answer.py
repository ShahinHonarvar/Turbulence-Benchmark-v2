def all_odd_ints_exclusive(int_list):
    return [num for idx, num in enumerate(int_list) if idx in range(1, 8) and num % 2 != 0]