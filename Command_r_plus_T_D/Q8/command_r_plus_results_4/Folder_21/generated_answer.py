def all_even_ints_exclusive(numbers_list: list[int]) -> list[int]:
    even_numbers = [num for num in numbers_list[743:867] if num % 2 == 0]
    return even_numbers