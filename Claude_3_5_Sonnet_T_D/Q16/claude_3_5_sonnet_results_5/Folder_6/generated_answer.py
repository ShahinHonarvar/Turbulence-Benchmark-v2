def sum_even_ints_inclusive(numbers):
    if len(numbers) <= 10:
        return 0
    end = min(67, len(numbers))
    return sum((num for num in numbers[10:end] if num % 2 == 0))