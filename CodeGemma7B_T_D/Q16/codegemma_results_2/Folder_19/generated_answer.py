def sum_even_ints_inclusive(int_list):
    if not any((n % 2 == 0 for n in int_list[3:6])):
        return 0
    else:
        return sum((n for n in int_list[3:6] if n % 2 == 0))