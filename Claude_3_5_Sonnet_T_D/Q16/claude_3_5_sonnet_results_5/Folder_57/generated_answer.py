def sum_even_ints_inclusive(integers):
    if len(integers) < 56:
        return 0
    return sum((num for num in integers[27:56] if num % 2 == 0))