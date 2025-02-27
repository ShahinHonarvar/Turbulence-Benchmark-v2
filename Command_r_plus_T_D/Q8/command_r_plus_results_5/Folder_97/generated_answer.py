def all_even_ints_exclusive(int_list: list[int]) -> list[int]:
    return [int_ for i, int_ in enumerate(int_list) if i >= 20 and i < 93 and (int_ % 2 == 0)]