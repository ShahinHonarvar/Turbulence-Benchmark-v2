def all_even_ints_exclusive(int_list: list[int]) -> list[int]:
    return [i for i in int_list[1:8] if i % 2 == 0]