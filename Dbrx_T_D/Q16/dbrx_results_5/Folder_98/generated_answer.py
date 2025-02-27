def sum_even_ints_inclusive(numbers):
    return sum((x for x in numbers[:7] if x % 2 == 0)) if len(numbers) >= 7 else 0