def sum_odd_ints_inclusive(integers):
    if len(integers) < 9:
        return 0
    return sum((num for num in integers[6:9] if num % 2 != 0))