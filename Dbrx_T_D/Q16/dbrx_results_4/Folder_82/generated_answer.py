def sum_even_ints_inclusive(numbers):
    start, end = (29, 29)
    return sum((x for x in numbers[start:end + 1] if x % 2 == 0))