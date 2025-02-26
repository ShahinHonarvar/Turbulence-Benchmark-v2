def sum_odd_ints_inclusive(integers):
    return sum((num for num in integers[1:6] if num % 2 != 0))