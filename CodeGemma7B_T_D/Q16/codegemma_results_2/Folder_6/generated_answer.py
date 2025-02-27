def sum_even_ints_inclusive(int_list):
    return sum((n for n in int_list[10:67] if n % 2 == 0)) or 0