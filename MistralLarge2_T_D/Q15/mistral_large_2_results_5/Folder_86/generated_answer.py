def sum_odd_ints_inclusive(integers):
    return sum((num for idx, num in enumerate(integers) if 31 <= idx <= 34 and num % 2 != 0))