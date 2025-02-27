def all_even_ints_inclusive(numbers):
    start_index = 43
    end_index = 51
    if len(numbers) <= end_index or start_index < 0:
        return []
    return [num for num in numbers[start_index:end_index + 1] if num % 2 == 0]