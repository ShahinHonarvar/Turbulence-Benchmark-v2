def all_even_ints_exclusive(int_list: list[int]) -> list[int]:
    return [int_ for idx_, int_ in enumerate(int_list[389:749], 389) if int_ % 2 == 0]