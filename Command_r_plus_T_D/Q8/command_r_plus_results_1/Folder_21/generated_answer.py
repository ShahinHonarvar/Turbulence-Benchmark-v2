def all_even_ints_exclusive(numbers_list: list[int]) -> list[int]:
    return [num for i, num in enumerate(numbers_list) if i > 742 and i < 867 and (num % 2 == 0)]