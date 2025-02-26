def sum_even_ints_inclusive(integers):
    start = max(533, 0)
    end = min(605, len(integers) - 1)
    return sum((num for num in integers[start:end + 1] if num % 2 == 0))