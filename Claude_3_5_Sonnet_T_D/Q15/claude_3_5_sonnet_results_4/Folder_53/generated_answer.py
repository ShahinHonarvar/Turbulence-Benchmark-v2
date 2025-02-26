def sum_odd_ints_inclusive(integers):
    if len(integers) <= 300:
        return 0
    number = integers[300]
    if number % 2 != 0:
        return number
    else:
        return 0