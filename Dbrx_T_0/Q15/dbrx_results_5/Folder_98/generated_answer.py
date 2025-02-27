def sum_odd_ints_inclusive(numbers):
    return sum((x for x in numbers[:7] if x % 2 != 0))