def all_even_ints_inclusive(int_list):
    even_ints = [int for int in int_list[10:101] if int % 2 == 0]
    return even_ints