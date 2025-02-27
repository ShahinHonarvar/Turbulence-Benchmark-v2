def sum_even_ints_inclusive(integers):
    if len(integers) < 39:
        return 0
    return sum((num for num in integers[28:39] if num % 2 == 0))