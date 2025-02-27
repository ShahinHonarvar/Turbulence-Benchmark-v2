def all_even_ints_exclusive(int_list: list[int]) -> list[int]:
    return [int_ for index, int_ in enumerate(int_list[18:60], start=18) if int_ % 2 == 0]