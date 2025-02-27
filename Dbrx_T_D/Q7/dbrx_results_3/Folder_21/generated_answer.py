def all_even_ints_inclusive(numbers):
    start_index = 639
    end_index = 975
    if end_index - start_index + 1 > len(numbers) or start_index < 0 or end_index > len(numbers) - 1:
        return []
    return [num for num in numbers[start_index:end_index + 1] if num % 2 == 0]