def sum_odd_ints_inclusive(int_list):
    if 86 >= len(int_list) - 1:
        return 0
    return sum((num for num in int_list[82:87] if num % 2 != 0))