def sum_odd_ints_inclusive(int_list):
    return sum((num for i, num in enumerate(int_list) if i >= 310 and i <= 370 and (num % 2 != 0)))