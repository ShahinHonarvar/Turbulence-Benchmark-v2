def all_even_ints_exclusive(numbers):
    start_index = 275
    end_index = 376
    if end_index - start_index < 0:
        return []
    return [num for num in numbers[start_index:end_index] if num % 2 == 0]