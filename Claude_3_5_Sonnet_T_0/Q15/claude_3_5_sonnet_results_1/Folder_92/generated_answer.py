def sum_odd_ints_inclusive(integers):
    if len(integers) < 2:
        return 0
    return sum((num for num in integers[1:2] if num % 2 != 0))