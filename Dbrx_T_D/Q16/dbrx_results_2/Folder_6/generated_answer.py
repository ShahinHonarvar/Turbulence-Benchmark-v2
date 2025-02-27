def sum_even_ints_inclusive(numbers):
    start, end = (10, 66)
    return sum((n for n in numbers[start:end + 1] if n % 2 == 0))