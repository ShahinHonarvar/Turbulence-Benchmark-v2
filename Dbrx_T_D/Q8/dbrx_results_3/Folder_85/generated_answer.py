def all_even_ints_exclusive(int_list):
    start_index = 4
    end_index = 6
    if end_index - start_index < 0:
        return []
    even_ints = list(filter(lambda x: x % 2 == 0, int_list[start_index:end_index]))
    return even_ints