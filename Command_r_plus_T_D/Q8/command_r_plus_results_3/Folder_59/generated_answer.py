def all_even_ints_exclusive(numbers_list: list[int]) -> list[int]:
    even_numbers = [num for i, num in enumerate(numbers_list) if num % 2 == 0 and i < 9 and (i > 0)]
    return even_numbers