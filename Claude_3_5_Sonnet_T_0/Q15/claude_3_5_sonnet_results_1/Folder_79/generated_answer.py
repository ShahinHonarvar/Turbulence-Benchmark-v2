def sum_odd_ints_inclusive(integers):
    if len(integers) < 5:
        return 0
    return sum((num for num in [integers[4]] if num % 2 != 0))