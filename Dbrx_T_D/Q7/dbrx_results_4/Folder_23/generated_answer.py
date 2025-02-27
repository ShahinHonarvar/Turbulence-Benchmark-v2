def all_even_ints_inclusive(numbers):
    start_index = 52
    end_index = 71
    if start_index < 0 or end_index >= len(numbers) or start_index > end_index:
        return []
    return [num for num in numbers[start_index:end_index + 1] if num % 2 == 0]