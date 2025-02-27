def all_even_ints_inclusive(int_list):
    if len(int_list) < 35:
        return []
    else:
        return [i for i in int_list[31:35] if i % 2 == 0]