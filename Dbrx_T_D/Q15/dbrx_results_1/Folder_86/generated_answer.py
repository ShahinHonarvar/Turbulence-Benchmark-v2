def sum_odd_ints_inclusive(numbers):
    odd_ints = sum(filter(lambda x: x % 2 != 0, numbers[31:35]))
    return odd_ints if odd_ints != 0 else 0