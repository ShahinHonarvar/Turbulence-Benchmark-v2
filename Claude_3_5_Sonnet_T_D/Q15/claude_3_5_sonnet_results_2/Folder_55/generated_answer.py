def sum_odd_ints_inclusive(integers):
    return sum((num for num in integers[:11] if num % 2 != 0))