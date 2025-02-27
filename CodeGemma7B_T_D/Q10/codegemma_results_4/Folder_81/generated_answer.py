def all_odd_ints_exclusive(int_list):
    range_list = int_list[10:11]
    return [num for num in range_list if num % 2 != 0] if range_list else []