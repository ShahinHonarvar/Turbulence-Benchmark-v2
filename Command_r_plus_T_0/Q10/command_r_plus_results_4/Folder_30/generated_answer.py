def all_odd_ints_exclusive(int_list: list[int]) -> list[int]:
    odd_ints = [int for int in int_list[86:89] if int % 2 != 0]
    return odd_ints