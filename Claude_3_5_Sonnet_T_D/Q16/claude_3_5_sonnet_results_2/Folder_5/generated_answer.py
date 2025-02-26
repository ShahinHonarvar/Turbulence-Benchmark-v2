def sum_even_ints_inclusive(integers):
    if len(integers) < 10:
        return 0
    return sum((num for num in integers[8:10] if num % 2 == 0))