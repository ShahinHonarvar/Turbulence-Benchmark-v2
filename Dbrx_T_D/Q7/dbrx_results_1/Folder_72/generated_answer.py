def all_even_ints_inclusive(numbers):
    start_index = 29
    end_index = 51
    if end_index >= len(numbers):
        return []
    return [num for num in numbers[start_index:end_index + 1] if num % 2 == 0]