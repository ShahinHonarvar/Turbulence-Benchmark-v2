def all_odd_ints_exclusive(int_list: list[int]) -> list[int]:
    odd_integers = [int_ for i, int_ in enumerate(int_list) if i >= 38 and i < 81 and (int_ % 2 != 0)]
    return odd_integers