def sum_odd_ints_inclusive(integers):
    if len(integers) < 94:
        return 0
    return sum((num for num in integers[66:94] if num % 2 != 0))