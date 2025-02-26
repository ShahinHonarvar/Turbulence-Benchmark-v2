def sum_even_ints_inclusive(integers):
    if len(integers) < 83:
        return 0
    return sum((num for num in integers[56:83] if num % 2 == 0))