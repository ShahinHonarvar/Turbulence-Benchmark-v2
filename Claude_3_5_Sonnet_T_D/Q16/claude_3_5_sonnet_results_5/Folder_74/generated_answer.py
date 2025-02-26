def sum_even_ints_inclusive(integers):
    if len(integers) < 79:
        return 0
    return sum((num for num in integers[17:79] if num % 2 == 0))