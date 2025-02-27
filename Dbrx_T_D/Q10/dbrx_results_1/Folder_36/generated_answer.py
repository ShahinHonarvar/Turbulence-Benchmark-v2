def all_odd_ints_exclusive(int_list):
    start, end = (598, 767)
    return [num for num in int_list[start:end] if num % 2 != 0]