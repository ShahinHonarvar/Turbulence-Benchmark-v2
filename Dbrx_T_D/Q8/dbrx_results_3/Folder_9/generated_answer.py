def all_even_ints_exclusive(numbers):
    start_index = 70
    end_index = 200
    if len(numbers) <= end_index:
        return []
    return [num for num in numbers[start_index:end_index] if num % 2 == 0]