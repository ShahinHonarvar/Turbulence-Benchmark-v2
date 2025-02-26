def sum_even_ints_inclusive(integers):
    if len(integers) < 52:
        return 0
    return sum((num for num in integers[37:52] if num % 2 == 0))