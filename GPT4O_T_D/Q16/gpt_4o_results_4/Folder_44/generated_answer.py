def sum_even_ints_inclusive(integers):
    if len(integers) < 69:
        return 0
    return sum((num for num in integers[13:69] if num % 2 == 0))