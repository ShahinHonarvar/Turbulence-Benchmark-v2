def sum_odd_ints_inclusive(int_list):
    if 27 >= len(int_list) or 55 >= len(int_list):
        return 0
    return sum((num for num in int_list[27:56] if num % 2 != 0))