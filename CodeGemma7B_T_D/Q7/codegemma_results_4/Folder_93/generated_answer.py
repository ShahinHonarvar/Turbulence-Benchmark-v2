def all_even_ints_inclusive(int_list):
    if not any((i % 2 == 0 for i in int_list[75:95])):
        return []
    return [i for i in int_list[75:95] if i % 2 == 0]