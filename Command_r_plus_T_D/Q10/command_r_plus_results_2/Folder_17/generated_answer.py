def all_odd_ints_exclusive(int_list: list[int]) -> list[int]:
    odd_integers = [int_ for int_ in int_list[62:96] if int_ % 2 != 0]
    return odd_integers