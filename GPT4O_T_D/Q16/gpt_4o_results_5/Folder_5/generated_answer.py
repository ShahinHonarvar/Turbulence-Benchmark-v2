def sum_even_ints_inclusive(numbers):
    if len(numbers) < 10:
        return 0
    return sum((x for x in numbers[8:10] if x % 2 == 0))