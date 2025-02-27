def all_even_ints_inclusive(int_list):
    return [int_list[i] for i in range(64, 67) if i < len(int_list) and int_list[i] % 2 == 0]