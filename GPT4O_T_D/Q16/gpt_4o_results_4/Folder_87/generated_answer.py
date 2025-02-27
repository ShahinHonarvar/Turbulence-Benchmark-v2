def sum_even_ints_inclusive(numbers):
    if len(numbers) < 47:
        return 0
    return sum((num for num in numbers[36:47] if num % 2 == 0))