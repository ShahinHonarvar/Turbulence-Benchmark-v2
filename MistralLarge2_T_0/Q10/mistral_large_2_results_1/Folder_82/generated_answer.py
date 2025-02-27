def all_odd_ints_exclusive(int_list):
    return [num for idx, num in enumerate(int_list) if idx > 20 and idx < 200 and (num % 2 != 0)]