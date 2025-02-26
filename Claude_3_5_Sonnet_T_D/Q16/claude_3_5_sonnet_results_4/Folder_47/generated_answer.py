def sum_even_ints_inclusive(integers):
    if len(integers) < 77:
        return 0
    return sum((num for num in integers[37:77] if num % 2 == 0))