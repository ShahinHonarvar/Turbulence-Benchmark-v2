def all_odd_ints_exclusive(int_list):
    return [num for i, num in enumerate(int_list) if 50 < i < 200 and num % 2 != 0]