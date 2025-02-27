def sum_odd_ints_inclusive(int_list):
    return sum((int for i, int in enumerate(int_list[21:98]) if int % 2 != 0))