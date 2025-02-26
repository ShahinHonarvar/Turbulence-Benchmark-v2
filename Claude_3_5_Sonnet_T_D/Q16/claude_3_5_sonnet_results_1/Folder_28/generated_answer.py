def sum_even_ints_inclusive(integers):
    if len(integers) < 64:
        return 0
    return sum((num for num in integers[62:64] if num % 2 == 0))