def all_even_ints_inclusive(my_list):
    if len(my_list) < 36:
        return []
    my_range = my_list[33:37]
    return [i for i in my_range if i % 2 == 0]