def sum_odd_ints_inclusive(int_list):
    if 40 < len(int_list) and 41 < len(int_list):
        return sum((num for num in int_list[40:42] if num % 2 != 0))
    return 0