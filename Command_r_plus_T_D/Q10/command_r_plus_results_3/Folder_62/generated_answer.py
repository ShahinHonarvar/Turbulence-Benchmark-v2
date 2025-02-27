def all_odd_ints_exclusive(int_list: list[int]) -> list[int]:
    odd_ints = [int_ for i, int_ in enumerate(int_list) if i >= 55 and i < 84 and (int_ % 2 != 0)]
    return odd_ints