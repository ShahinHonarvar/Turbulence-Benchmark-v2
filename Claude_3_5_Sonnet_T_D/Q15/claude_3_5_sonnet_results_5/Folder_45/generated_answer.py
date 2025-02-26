def sum_odd_ints_inclusive(integers):
    start = 30
    end = 201
    return sum((num for num in integers[start:end] if num % 2 != 0))