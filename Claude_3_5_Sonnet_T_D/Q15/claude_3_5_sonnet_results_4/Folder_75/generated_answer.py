def sum_odd_ints_inclusive(integers):
    if len(integers) < 58:
        return 0
    return sum((num for num in integers[56:58] if num % 2 != 0))