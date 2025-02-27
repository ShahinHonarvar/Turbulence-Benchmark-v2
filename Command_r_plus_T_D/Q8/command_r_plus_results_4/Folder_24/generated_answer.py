def all_even_ints_exclusive(int_list: list[int]) -> list[int]:
    return [int_ for i, int_ in enumerate(int_list[13:66]) if int_ % 2 == 0]