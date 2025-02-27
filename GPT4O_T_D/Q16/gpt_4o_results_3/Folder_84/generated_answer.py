def sum_even_ints_inclusive(integers):
    if len(integers) < 87:
        return 0
    return sum((num for num in integers[43:87] if num % 2 == 0))