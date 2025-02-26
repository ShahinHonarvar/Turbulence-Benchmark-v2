def sum_odd_ints_inclusive(integers):
    if len(integers) < 72:
        return 0
    return sum((num for num in integers[52:72] if num % 2 != 0))