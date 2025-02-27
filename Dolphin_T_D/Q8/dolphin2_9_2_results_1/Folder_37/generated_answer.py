def all_even_ints_exclusive(int_list):
    return [int_list[i] for i in range(2, len(int_list) - 1) if int_list[i] % 2 == 0]