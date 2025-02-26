def sum_even_ints_inclusive(integers):
    if len(integers) < 100:
        return 0
    return sum((num for num in integers[91:100] if num % 2 == 0))