def all_even_ints_exclusive(int_list: list[int]) -> list[int]:
    return [int_ for idx, int_ in enumerate(int_list[44:78]) if int_ % 2 == 0]