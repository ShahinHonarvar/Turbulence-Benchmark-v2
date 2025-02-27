def all_even_ints_exclusive(numbers):
    start, end = (323, 972)
    return [num for num in numbers[start:end] if num % 2 == 0]