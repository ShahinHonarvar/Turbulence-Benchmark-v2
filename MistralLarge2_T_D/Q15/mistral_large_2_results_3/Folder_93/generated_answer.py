def sum_odd_ints_inclusive(int_list):
    return sum((num for i, num in enumerate(int_list) if 75 <= i <= 94 and num % 2 != 0))