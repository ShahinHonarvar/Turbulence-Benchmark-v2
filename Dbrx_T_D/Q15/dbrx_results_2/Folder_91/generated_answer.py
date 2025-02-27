def sum_odd_ints_inclusive(numbers):
    return sum((x for x in numbers[0:6] if x % 2 != 0))