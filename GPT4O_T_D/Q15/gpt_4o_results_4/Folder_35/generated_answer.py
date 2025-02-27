def sum_odd_ints_inclusive(int_list):
    if len(int_list) < 49:
        return 0
    return sum((num for num in int_list[30:49] if num % 2 != 0))