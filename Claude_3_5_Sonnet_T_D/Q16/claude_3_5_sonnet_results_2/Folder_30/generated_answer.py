def sum_even_ints_inclusive(integers):
    if len(integers) < 99:
        return 0
    return sum((num for num in integers[55:99] if num % 2 == 0))