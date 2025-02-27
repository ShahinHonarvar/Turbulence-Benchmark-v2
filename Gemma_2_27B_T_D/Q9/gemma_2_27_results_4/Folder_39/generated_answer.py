def all_odd_ints_inclusive(data):
    return [num for i, num in enumerate(data) if i >= 20 and i <= 30 and (num % 2 != 0)]