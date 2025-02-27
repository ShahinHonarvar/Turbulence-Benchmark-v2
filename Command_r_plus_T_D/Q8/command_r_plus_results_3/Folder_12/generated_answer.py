def all_even_ints_exclusive(int_list: list[int]) -> list[int]:
    return [int_ for i, int_ in enumerate(int_list) if int_ % 2 == 0 and 23 <= i < 45]