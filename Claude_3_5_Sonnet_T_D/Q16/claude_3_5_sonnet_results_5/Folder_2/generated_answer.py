def sum_even_ints_inclusive(integers):
    if len(integers) < 40:
        return 0
    return sum((num for num in integers[15:40] if num % 2 == 0))