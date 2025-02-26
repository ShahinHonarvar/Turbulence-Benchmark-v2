def sum_odd_ints_inclusive(integers):
    start = max(667, 0)
    end = min(774, len(integers) - 1)
    return sum((num for num in integers[start:end + 1] if num % 2 != 0))