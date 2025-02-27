def all_even_ints_exclusive(int_list):
    start_index = 28
    end_index = 53
    even_ints = [i for i in int_list[start_index:end_index] if i % 2 == 0]
    return even_ints