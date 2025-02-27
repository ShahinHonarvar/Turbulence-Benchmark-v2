def sum_odd_ints_inclusive(numbers):
    return sum((num for i, num in enumerate(numbers[13:69]) if num % 2 != 0))