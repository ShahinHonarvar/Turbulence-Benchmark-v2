def all_even_ints_exclusive(int_list):
    if not int_list:
        return []
    even_ints = [n for n in int_list[20:93] if n % 2 == 0]
    return even_ints or []