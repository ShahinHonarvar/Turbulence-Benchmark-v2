def all_even_ints_exclusive(int_list):
    even_ints = [int_list[i] for i in range(323, 972) if int_list[i] % 2 == 0]
    return even_ints