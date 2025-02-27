def all_odd_ints_exclusive(int_list: list[int]) -> list[int]:
    odd_integers = [int_ for idx, int_ in enumerate(int_list) if idx >= 56 and idx < 92 and (int_ % 2 != 0)]
    return odd_integers