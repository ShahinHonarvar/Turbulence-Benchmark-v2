def sum_even_ints_inclusive(numbers):
    start, end = (12, 92)
    return sum((num for num in numbers[start:end + 1] if num % 2 == 0))