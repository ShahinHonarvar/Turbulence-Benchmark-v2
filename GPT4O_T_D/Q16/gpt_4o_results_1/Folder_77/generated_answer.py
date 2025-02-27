def sum_even_ints_inclusive(numbers):
    if len(numbers) < 539:
        return 0
    return sum((num for num in numbers[527:539] if num % 2 == 0))