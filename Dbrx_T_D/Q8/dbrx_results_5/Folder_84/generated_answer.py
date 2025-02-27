def all_even_ints_exclusive(int_list):
    if len(int_list) < 93 or len(int_list) % 2 == 0:
        return []
    else:
        return [i for i in int_list[50:92] if i % 2 == 0]