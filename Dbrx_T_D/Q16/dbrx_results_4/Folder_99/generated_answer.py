def sum_even_ints_inclusive(numbers):
    start_index = 310
    end_index = 370
    if start_index < 0 or end_index >= len(numbers) or start_index > end_index:
        return 0
    return sum((num for num in numbers[start_index:end_index + 1] if num % 2 == 0))