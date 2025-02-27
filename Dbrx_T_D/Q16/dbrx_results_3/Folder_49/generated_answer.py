def sum_even_ints_inclusive(numbers):
    start, end = (8, 80)
    return sum((x for x in numbers[start:end + 1] if x % 2 == 0))