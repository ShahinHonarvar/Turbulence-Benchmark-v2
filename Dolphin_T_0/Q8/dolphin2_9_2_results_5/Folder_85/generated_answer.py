def all_even_ints_exclusive(int_list):
    return [int for i, int in enumerate(int_list) if 4 < i < 6 and int % 2 == 0]