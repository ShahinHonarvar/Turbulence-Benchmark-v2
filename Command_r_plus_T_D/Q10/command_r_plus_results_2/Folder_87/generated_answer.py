def all_odd_ints_exclusive(int_list: list[int]) -> list[int]:
    odd_integers = [int_ for i, int_ in enumerate(int_list) if int_ % 2 != 0 and 32 <= i < 99]
    return odd_integers