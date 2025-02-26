def sum_odd_ints_inclusive(integers):
    start = 36
    end = 47
    return sum((num for num in integers[start:end] if num % 2 != 0))