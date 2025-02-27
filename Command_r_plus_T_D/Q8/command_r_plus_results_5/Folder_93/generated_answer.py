def all_even_ints_exclusive(int_list: list[int]) -> list[int]:
    even_ints = [int_ for int_ in int_list[19:94] if int_ % 2 == 0]
    return even_ints