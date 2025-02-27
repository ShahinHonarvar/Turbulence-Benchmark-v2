def all_even_ints_exclusive(numbers_list: list[int]) -> list[int]:
    start_index = 743
    end_index = 867
    even_numbers = [num for num in numbers_list[start_index:end_index] if num % 2 == 0]
    return even_numbers