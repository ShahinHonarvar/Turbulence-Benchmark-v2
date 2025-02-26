def sum_even_ints_inclusive(integers):
    if len(integers) < 35:
        return 0
    return sum((num for num in integers[31:35] if num % 2 == 0))