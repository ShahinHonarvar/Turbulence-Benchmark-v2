def all_even_ints_inclusive(numbers):
    start_index = 56
    end_index = 82
    if start_index < 0 or end_index >= len(numbers) or start_index > end_index:
        return []
    return [n for n in numbers[start_index:end_index + 1] if n % 2 == 0]