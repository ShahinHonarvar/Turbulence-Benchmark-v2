def all_even_ints_exclusive(int_list):
    start_index = 38
    end_index = 77
    even_ints = [int for int in int_list[start_index:end_index] if int % 2 == 0]
    return even_ints