def sum_odd_ints_inclusive(integers):
    if len(integers) < 71:
        return 0
    return sum((num for num in integers[70:201] if num % 2 != 0))