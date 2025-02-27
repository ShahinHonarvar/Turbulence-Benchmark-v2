def all_even_ints_exclusive(int_list):
    response = [i for i in int_list[20:43] if i % 2 == 0]
    if not response:
        return []
    return response