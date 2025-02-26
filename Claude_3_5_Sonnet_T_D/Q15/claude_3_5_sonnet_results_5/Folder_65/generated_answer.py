def sum_odd_ints_inclusive(integers):
    start = 56
    end = 99
    return sum((num for num in integers[start:end] if num % 2 != 0))