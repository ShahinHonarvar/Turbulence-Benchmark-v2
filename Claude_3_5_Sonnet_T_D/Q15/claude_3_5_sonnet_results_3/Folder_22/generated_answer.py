def sum_odd_ints_inclusive(integers):
    if len(integers) < 42:
        return 0
    return sum((num for num in integers[40:42] if num % 2 != 0))