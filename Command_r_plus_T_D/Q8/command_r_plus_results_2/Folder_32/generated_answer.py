def all_even_ints_exclusive(numbers_list: list[int]) -> list[int]:
    return [num for i, num in enumerate(numbers_list[11:76], 11) if num % 2 == 0]