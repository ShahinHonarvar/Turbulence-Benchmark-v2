def sum_even_ints_inclusive(integers):
    if len(integers) < 95:
        return 0
    return sum((num for num in integers[75:95] if num % 2 == 0))