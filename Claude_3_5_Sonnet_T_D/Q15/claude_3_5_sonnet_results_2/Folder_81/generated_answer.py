def sum_odd_ints_inclusive(integers):
    return sum((num for num in integers[10:101] if num % 2 != 0))