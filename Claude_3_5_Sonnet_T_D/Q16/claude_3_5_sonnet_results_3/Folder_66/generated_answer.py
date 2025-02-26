def sum_even_ints_inclusive(numbers):
    if len(numbers) < 55:
        return 0
    return sum((num for num in numbers[50:55] if num % 2 == 0))