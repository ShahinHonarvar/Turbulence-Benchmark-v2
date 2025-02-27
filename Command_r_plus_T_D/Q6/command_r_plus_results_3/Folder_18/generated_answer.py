def all_neg_ints_exclusive(int_list: list[int]) -> list[int]:
    return [int_ for idx, int_ in enumerate(int_list[57:84]) if int_ < 0]