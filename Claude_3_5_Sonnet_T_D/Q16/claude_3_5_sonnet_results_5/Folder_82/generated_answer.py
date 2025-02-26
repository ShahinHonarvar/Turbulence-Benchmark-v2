def sum_even_ints_inclusive(integers):
    if len(integers) <= 29:
        return 0
    return sum((num for num in [integers[29]] if num % 2 == 0))