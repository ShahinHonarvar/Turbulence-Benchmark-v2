def all_even_ints_exclusive(my_list):
    if len(my_list) < 98:
        return []
    return [i for i in my_list[70:98] if i % 2 == 0]