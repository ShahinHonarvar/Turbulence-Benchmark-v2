def all_even_ints_exclusive(int_list: list[int]) -> list[int]:
    return [num for i, num in enumerate(int_list) if num % 2 == 0 and i < 8]