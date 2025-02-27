def all_even_ints_exclusive(int_list: list[int]) -> list[int]:
    return [num for i, num in enumerate(int_list) if i >= 44 and i < 78 and (num % 2 == 0)]