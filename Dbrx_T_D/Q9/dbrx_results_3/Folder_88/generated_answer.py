from functools import reduce

def all_odd_ints_inclusive(numbers):
    odd_numbers = filter(lambda x: x % 2 != 0, numbers[4:9])
    return list(reduce(lambda a, b: a + [b], odd_numbers, []))