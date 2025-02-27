def sum_even_ints_inclusive(numbers):
    if len(numbers) < 2:
        return 0
    return sum((num for num in numbers[0:2] if num % 2 == 0))