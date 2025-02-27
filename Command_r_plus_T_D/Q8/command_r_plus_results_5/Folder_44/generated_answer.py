def all_even_ints_exclusive(int_list: list[int]) -> list[int]:
    return [int for i, int in enumerate(int_list) if int % 2 == 0 and 81 <= i < 86]