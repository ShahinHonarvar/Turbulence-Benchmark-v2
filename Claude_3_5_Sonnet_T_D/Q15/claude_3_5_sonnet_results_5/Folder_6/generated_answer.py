def sum_odd_ints_inclusive(numbers):
    start = 10
    end = min(67, len(numbers))
    return sum((num for num in numbers[start:end] if num % 2 != 0))