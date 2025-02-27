def all_even_ints_exclusive(int_list):
    if len(int_list) < 200:
        return []
    even_ints = [i for i in int_list[50:200] if i % 2 == 0]
    return even_ints