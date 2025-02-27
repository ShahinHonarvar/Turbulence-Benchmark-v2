def all_even_ints_exclusive(int_list: list[int]) -> list[int]:
    return [int_ for idx_, int_ in enumerate(int_list) if idx_ >= 86 and idx_ < 99 and (int_ % 2 == 0)]