def sum_even_ints_inclusive(numbers):
    if not numbers or len(numbers) < 2:
        return 0
    return sum(filter(lambda x: x % 2 == 0, numbers[:2]))