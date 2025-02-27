def sum_even_ints_inclusive(numbers):
    return sum((x for x in numbers[min(1, len(numbers) - 5):min(5, len(numbers))] if x % 2 == 0))