def sum_odd_ints_inclusive(int_list):
    if 22 >= len(int_list) or 88 >= len(int_list):
        return 0
    return sum((num for num in int_list[22:89] if num % 2 != 0))