def sum_odd_ints_inclusive(int_list):
    return sum((int for i, int in enumerate(int_list) if 19 <= i <= 92 and int % 2 != 0))