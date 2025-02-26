def sum_even_ints_inclusive(integers):
    start = 12
    end = min(92, len(integers) - 1)
    return sum((num for num in integers[start:end + 1] if num % 2 == 0))