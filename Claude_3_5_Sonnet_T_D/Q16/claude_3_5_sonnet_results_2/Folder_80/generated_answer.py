def sum_even_ints_inclusive(integers):
    if len(integers) < 67:
        return 0
    return sum((num for num in integers[64:67] if num % 2 == 0))