def sum_even_ints_inclusive(numbers):
    if len(numbers) < 2:
        return 0
    return sum((x for x in numbers[:2] if x % 2 == 0))