def all_even_ints_exclusive(numbers_list: list[int]) -> list[int]:
    even_integers = [num for num in numbers_list[276:376] if num % 2 == 0]
    return even_integers