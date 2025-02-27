def all_even_ints_exclusive(int_list):
    if len(int_list) < 92:
        return []
    return [i for i in int_list[50:92] if i % 2 == 0]