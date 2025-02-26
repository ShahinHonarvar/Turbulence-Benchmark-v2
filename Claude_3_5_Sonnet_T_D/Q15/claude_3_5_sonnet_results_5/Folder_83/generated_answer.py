def sum_odd_ints_inclusive(integers):
    start = 90
    end = min(200, len(integers) - 1)
    return sum((num for num in integers[start:end + 1] if num % 2 != 0))