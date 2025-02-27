def all_even_ints_exclusive(int_list: list[int]) -> list[int]:
    return [int_ for idx, int_ in enumerate(int_list) if idx > 85 and idx < 90 and (int_ % 2 == 0)]