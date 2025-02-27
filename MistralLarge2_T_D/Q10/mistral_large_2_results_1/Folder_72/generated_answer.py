def all_odd_ints_exclusive(int_list):
    return [num for idx, num in enumerate(int_list) if idx > 56 and idx < 88 and (num % 2 != 0)]