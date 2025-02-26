def sum_odd_ints_inclusive(integers):
    if len(integers) < 86:
        return 0
    return sum((num for num in integers[75:86] if num % 2 != 0))