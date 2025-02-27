def all_odd_ints_exclusive(int_list: list[int]) -> list[int]:
    odd_ints = [int for i, int in enumerate(int_list) if int % 2 != 0 and i < 9]
    return odd_ints[:10]