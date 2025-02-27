def all_even_ints_inclusive(numbers):
    start, end = (26, 52)
    return [num for num in numbers[start:end + 1] if num % 2 == 0]