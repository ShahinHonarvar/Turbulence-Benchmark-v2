def sum_odd_ints_inclusive(integers):
    if len(integers) < 88:
        return 0
    return sum((num for num in integers[30:88] if num % 2 != 0))