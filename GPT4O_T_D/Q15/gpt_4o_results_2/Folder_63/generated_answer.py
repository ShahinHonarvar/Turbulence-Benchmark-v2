def sum_odd_ints_inclusive(numbers):
    if len(numbers) < 89:
        return 0
    return sum((n for n in numbers[22:89] if n % 2 != 0))