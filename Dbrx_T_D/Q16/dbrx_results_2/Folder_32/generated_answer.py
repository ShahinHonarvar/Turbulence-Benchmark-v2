def sum_even_ints_inclusive(int_list):
    if len(int_list) < 97:
        return 'List is too short'
    else:
        return sum((x for x in int_list[20:98] if x % 2 == 0))