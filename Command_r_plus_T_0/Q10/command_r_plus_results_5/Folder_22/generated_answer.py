def all_odd_ints_exclusive(int_list: list[int]) -> list[int]:
    odd_ints = [int_ for int_ in int_list[40:200] if int_ % 2 != 0]
    return odd_ints