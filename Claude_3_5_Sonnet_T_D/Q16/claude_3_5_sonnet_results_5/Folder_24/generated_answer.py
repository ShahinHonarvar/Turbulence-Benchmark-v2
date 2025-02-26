def sum_even_ints_inclusive(integers):
    if len(integers) < 96:
        return 0
    return sum((num for num in integers[74:96] if num % 2 == 0))