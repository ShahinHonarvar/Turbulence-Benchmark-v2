def sum_odd_ints_inclusive(integers):
    start = 37
    end = 77
    if len(integers) < end:
        end = len(integers)
    return sum((num for num in integers[start:end] if num % 2 != 0))