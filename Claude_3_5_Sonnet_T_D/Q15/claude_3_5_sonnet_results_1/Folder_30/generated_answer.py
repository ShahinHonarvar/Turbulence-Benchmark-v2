def sum_odd_ints_inclusive(integers):
    start = 55
    end = 98
    if len(integers) <= start:
        return 0
    end = min(end, len(integers) - 1)
    return sum((num for num in integers[start:end + 1] if num % 2 != 0))