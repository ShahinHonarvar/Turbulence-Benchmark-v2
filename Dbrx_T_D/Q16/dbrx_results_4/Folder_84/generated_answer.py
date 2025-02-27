def sum_even_ints_inclusive(numbers):
    return sum((x for x in numbers[43:87] if x % 2 == 0)) if len(numbers) >= 87 else 0