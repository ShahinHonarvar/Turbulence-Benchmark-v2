def all_odd_ints_exclusive(int_list: list[int]) -> list[int]:
    odd_ints_in_range = [int_ for i, int_ in enumerate(int_list) if int_ % 2 != 0 and 44 <= i < 67]
    return odd_ints_in_range