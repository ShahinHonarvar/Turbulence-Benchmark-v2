def sum_even_ints_inclusive(integers):
    if len(integers) < 49:
        return 0
    return sum((num for num in integers[30:49] if num % 2 == 0))