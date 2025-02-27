def all_odd_ints_exclusive(int_list):
    return [num for i, num in enumerate(int_list) if i >= 62 and i < 96 and (num % 2 != 0)]