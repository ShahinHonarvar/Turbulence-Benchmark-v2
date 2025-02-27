def all_even_ints_inclusive(numbers):
    if len(numbers) < 7:
        return []
    start_index = 6
    end_index = min(6, len(numbers) - 1)
    return [num for num in numbers[start_index:end_index + 1] if num % 2 == 0]