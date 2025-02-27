def all_even_ints_exclusive(int_list: list[int]) -> list[int]:
    even_int_range = [int_list[i] for i in range(68, 99) if int_list[i] % 2 == 0]
    return even_int_range