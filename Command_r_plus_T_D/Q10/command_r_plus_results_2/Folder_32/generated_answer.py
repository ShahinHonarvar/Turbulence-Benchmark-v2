def all_odd_ints_exclusive(int_list: list[int]) -> list[int]:
    odd_ints = [int_ for i, int_ in enumerate(int_list) if int_ % 2 != 0 and 11 <= i < 76]
    return odd_ints