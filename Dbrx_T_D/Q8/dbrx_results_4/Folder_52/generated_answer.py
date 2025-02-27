def all_even_ints_exclusive(numbers):
    start_index = 93
    end_index = 94
    if start_index < 0 or end_index > len(numbers) or start_index >= end_index:
        return []
    return [num for num in numbers[start_index:end_index] if num % 2 == 0]