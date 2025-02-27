def all_odd_ints_exclusive(int_list):
    return [num for idx, num in enumerate(int_list) if num % 2 != 0 and 0 < idx < 9]