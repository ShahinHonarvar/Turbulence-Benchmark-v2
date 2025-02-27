def sum_even_ints_inclusive(numbers):
    return sum((x for x in numbers[:3] if x % 2 == 0))