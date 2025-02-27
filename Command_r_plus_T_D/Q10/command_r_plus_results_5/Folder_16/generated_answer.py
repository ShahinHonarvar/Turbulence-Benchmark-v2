def all_odd_ints_exclusive(int_list: list[int]) -> list[int]:
    return [int_ for i, int_ in enumerate(int_list) if i >= 86 and i < 90 and (int_ % 2 != 0)]