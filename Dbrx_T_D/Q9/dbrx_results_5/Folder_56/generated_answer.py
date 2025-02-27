def all_odd_ints_inclusive(numbers):
    odd_ints = [i for i in numbers[:2] if i % 2 != 0]
    return odd_ints