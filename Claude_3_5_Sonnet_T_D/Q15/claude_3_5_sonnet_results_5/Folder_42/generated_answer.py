def sum_odd_ints_inclusive(numbers):
    start = 29
    end = min(80, len(numbers))
    return sum((num for num in numbers[start:end] if num % 2 != 0))