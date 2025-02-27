def sum_even_ints_inclusive(int_list):
    if len(int_list) < 21:
        return 'List too short to find sum of even integers in the specified range.'
    else:
        return sum((x for x in int_list[21:98] if x % 2 == 0))