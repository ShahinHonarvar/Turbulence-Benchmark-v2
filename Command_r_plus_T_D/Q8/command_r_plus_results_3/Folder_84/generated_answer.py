def all_even_ints_exclusive(int_list: list[int]) -> list[int]:
    return [int_ for index, int_ in enumerate(int_list) if index >= 50 and index < 92 and (int_ % 2 == 0)]