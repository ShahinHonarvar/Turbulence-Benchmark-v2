def all_even_ints_exclusive(int_list: list[int]) -> list[int]:
    even_ints = [int for i, int in enumerate(int_list[18:60], 18) if int % 2 == 0]
    return even_ints