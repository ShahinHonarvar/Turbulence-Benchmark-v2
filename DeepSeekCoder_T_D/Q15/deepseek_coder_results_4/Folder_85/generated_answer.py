def sum_odd_ints_inclusive(int_list):
    if 6 < len(int_list) and 8 < len(int_list):
        return sum((num for num in int_list[6:9] if num % 2 != 0))
    return 0