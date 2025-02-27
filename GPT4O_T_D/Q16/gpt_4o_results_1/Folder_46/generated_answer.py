def sum_even_ints_inclusive(numbers):
    if not numbers or len(numbers) < 88:
        return 0
    return sum((num for num in numbers[30:88] if num % 2 == 0))