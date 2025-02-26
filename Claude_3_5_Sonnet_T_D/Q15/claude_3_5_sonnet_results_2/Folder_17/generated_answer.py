def sum_odd_ints_inclusive(integers):
    start = 62
    end = 79
    if len(integers) < end:
        end = len(integers)
    return sum((num for num in integers[start:end] if num % 2 != 0))