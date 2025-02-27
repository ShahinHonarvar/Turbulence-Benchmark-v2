def all_even_ints_exclusive(int_list: list[int]) -> list[int]:
    return [num for i, num in enumerate(int_list) if i >= 32 and i < 99 and (num % 2 == 0)]