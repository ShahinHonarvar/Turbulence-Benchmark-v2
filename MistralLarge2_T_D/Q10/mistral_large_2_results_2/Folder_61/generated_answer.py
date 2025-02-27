def all_odd_ints_exclusive(int_list):
    return [num for idx, num in enumerate(int_list) if idx > 0 and idx < 7 and (num % 2 != 0)]