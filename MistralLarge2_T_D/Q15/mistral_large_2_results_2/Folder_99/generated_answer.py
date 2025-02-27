def sum_odd_ints_inclusive(int_list):
    return sum((num for idx, num in enumerate(int_list) if 310 <= idx <= 370 and num % 2 != 0))