def all_even_ints_exclusive(numbers):
    start, end = (743, 867)
    return [num for num in numbers[start:end] if num % 2 == 0]