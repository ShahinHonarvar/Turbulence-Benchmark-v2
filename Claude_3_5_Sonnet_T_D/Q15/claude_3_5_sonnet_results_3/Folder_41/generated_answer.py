def sum_odd_ints_inclusive(integers):
    if len(integers) < 7:
        return 0
    return sum((num for num in [integers[6]] if num % 2 != 0))