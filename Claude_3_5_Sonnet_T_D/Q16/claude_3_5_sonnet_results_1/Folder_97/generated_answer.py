def sum_even_ints_inclusive(integers):
    if len(integers) < 81:
        return 0
    return sum((num for num in integers[40:81] if num % 2 == 0))