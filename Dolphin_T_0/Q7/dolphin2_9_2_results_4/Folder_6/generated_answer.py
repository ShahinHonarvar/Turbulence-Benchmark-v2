def all_even_ints_inclusive(int_list):
    even_ints = [int for i, int in enumerate(int_list) if i in range(10, 67) and int % 2 == 0]
    return even_ints