def sum_odd_ints_inclusive(integers):
    if len(integers) < 69:
        return sum((num for num in integers[13:] if num % 2 != 0))
    else:
        return sum((num for num in integers[13:69] if num % 2 != 0))