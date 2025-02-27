def all_even_ints_exclusive(int_list):
    if len(int_list) < 53:
        return []
    else:
        return [i for i in int_list[36:52] if i % 2 == 0]