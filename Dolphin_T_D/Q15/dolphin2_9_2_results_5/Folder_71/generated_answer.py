def sum_odd_ints_inclusive(numbers):
    return sum((num for i, num in enumerate(numbers[26:53]) if i % 2 != 0)) if any((num for i, num in enumerate(numbers[26:53]) if i % 2 != 0)) else 0