def all_even_ints_inclusive(int_list):
    if not isinstance(int_list, list) or len(int_list) < 60:
        return []
    return [x for x in int_list[25:60] if x % 2 == 0]