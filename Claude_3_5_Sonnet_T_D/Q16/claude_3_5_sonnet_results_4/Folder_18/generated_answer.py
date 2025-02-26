def sum_even_ints_inclusive(integers):
    if len(integers) < 50:
        return 0
    return sum((num for num in integers[35:50] if num % 2 == 0))