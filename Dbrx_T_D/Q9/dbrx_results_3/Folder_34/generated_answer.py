def all_odd_ints_inclusive(numbers):
    odd_ints = [n for n in numbers[60:] if n % 2 != 0]
    return odd_ints[51::-1] + odd_ints[:51:1]