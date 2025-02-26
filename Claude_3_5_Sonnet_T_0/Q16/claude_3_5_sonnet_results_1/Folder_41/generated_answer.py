def sum_even_ints_inclusive(integers):
    if len(integers) <= 6:
        return 0
    return sum((num for num in [integers[6]] if num % 2 == 0))