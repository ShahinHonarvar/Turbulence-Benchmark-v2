def all_even_ints_exclusive(int_list: list[int]) -> list[int]:
    even_ints = [int for int in int_list[1:4] if int % 2 == 0]
    return even_ints