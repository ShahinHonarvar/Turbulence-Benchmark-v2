def sum_even_ints_inclusive(numbers):
    if len(numbers) < 61:
        return 0
    return sum((num for num in numbers[60:201] if num % 2 == 0))