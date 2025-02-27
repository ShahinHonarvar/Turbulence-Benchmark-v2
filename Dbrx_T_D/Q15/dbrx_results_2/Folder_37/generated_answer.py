def sum_odd_ints_inclusive(numbers):
    return sum((x for x in numbers[1:6] if x % 2 != 0))