def sum_odd_ints_inclusive(integers):
    if len(integers) < 79:
        return 0
    return sum((num for num in integers[62:79] if num % 2 != 0))