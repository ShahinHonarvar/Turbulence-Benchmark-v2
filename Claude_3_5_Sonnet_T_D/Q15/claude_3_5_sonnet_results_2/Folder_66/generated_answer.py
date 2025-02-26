def sum_odd_ints_inclusive(integers):
    if len(integers) < 55:
        return 0
    return sum((num for num in integers[50:55] if num % 2 != 0))