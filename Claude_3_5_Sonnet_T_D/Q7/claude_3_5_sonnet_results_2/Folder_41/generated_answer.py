def all_even_ints_inclusive(integer_list):
    if len(integer_list) < 7:
        return []
    return [integer_list[6]] if integer_list[6] % 2 == 0 else []