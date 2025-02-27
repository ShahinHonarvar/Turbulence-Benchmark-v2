def sum_odd_ints_inclusive(numbers):
    return sum((i for i in numbers[:10] if i % 2 != 0))