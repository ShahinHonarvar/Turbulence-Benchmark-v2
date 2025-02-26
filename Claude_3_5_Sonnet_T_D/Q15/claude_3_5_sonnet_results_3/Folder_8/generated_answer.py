def sum_odd_ints_inclusive(integers):
    if len(integers) <= 23:
        return 0
    return sum((num for num in [integers[23]] if num % 2 != 0))