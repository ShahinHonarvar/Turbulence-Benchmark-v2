def all_even_ints_exclusive(int_list):
    if len(int_list) < 46:
        return []
    even_ints = [int_list[i] for i in range(23, 45) if int_list[i] % 2 == 0]
    return even_ints