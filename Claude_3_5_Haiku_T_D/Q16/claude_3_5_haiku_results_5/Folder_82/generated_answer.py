def sum_even_ints_inclusive(numbers):
    if 29 < len(numbers):
        value = numbers[29]
        return value if value % 2 == 0 else 0
    return 0