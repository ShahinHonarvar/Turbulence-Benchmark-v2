def all_odd_ints_exclusive(int_list: list[int]) -> list[int]:
    odd_range = [int_ for idx, int_ in enumerate(int_list) if (idx >= 64 and idx < 80) and int_ % 2 != 0]
    return odd_range