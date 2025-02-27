def all_odd_ints_exclusive(int_list: list[int]) -> list[int]:
    odd_ints_range = [int_ for idx_, int_ in enumerate(int_list[20:43]) if int_ % 2 != 0]
    return odd_ints_range