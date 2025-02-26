def sum_odd_ints_inclusive(integers):
    if len(integers) < 89:
        return 0
    return sum((num for num in integers[75:89] if num % 2 != 0))