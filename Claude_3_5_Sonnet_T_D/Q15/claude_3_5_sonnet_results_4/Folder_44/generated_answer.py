def sum_odd_ints_inclusive(integers):
    start = 13
    end = 69
    return sum((num for num in integers[start:end] if num % 2 != 0)) if len(integers) > start else 0