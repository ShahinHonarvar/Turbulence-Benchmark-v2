def all_even_ints_exclusive(int_list):
    if len(int_list) >= 100:
        return [i for i in int_list[15:99:2]]
    else:
        return []