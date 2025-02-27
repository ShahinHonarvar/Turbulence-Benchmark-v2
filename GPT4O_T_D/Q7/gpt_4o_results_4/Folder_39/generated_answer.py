def all_even_ints_inclusive(int_list):
    if len(int_list) < 21:
        return []
    sliced_list = int_list[20:31]
    return [x for x in sliced_list if x % 2 == 0]