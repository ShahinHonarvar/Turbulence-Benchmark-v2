def all_even_ints_exclusive(int_list: list[int]) -> list[int]:
    even_ints = [int for i, int in enumerate(int_list) if int % 2 == 0 and 10 <= i < 100]
    return even_ints