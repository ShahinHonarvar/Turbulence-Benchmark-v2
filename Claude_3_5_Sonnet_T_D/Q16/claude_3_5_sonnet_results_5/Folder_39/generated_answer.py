def sum_even_ints_inclusive(integers):
    if len(integers) < 31:
        return 0
    return sum((num for num in integers[20:31] if num % 2 == 0))