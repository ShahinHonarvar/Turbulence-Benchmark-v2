def sum_odd_ints_inclusive(int_list):
    return sum(int_list[19:93]) if any((num % 2 != 0 for num in int_list[19:93])) else 0