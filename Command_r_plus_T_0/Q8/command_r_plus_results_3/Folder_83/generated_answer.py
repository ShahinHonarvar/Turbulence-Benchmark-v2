def all_even_ints_exclusive(int_list):
    even_ints = [int for i, int in enumerate(int_list[90:200]) if int % 2 == 0]
    return even_ints