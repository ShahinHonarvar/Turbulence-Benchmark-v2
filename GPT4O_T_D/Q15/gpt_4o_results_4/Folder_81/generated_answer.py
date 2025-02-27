def sum_odd_ints_inclusive(numbers):
    if len(numbers) < 11:
        return 0
    return sum((n for n in numbers[10:101] if n % 2 != 0))