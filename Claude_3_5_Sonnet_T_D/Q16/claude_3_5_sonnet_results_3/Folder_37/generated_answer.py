def sum_even_ints_inclusive(integers):
    if len(integers) < 6:
        return sum((num for num in integers[1:] if num % 2 == 0))
    else:
        return sum((num for num in integers[1:6] if num % 2 == 0))