def all_odd_ints_inclusive(numbers):
    result = [n for i, n in enumerate(numbers[75:89]) if n % 2 != 0]
    return result