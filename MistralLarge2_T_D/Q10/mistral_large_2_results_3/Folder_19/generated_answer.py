def all_odd_ints_exclusive(int_list):
    return [num for i, num in enumerate(int_list) if num % 2 != 0 and 2 < i < 5]