def all_odd_ints_inclusive(numbers):
    odd_ints = [x for x in numbers[4:9] if isinstance(x, int) and x % 2 != 0]
    return odd_ints