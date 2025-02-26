def sum_odd_ints_inclusive(numbers):
    return sum((num for num in numbers[:9] if num % 2 != 0))