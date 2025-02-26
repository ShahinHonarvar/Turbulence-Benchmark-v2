def sum_even_ints_inclusive(integers):
    if len(integers) < 85:
        return 0
    return sum((num for num in integers[70:85] if num % 2 == 0))