def sum_even_ints_inclusive(numbers):
    if len(numbers) <= 30:
        return 0
    end_index = min(200, len(numbers) - 1)
    even_sum = sum((num for num in numbers[30:end_index + 1] if num % 2 == 0))
    return even_sum