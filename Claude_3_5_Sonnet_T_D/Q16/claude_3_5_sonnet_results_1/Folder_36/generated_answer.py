def sum_even_ints_inclusive(integers):
    start = max(246, 0)
    end = min(750, len(integers) - 1)
    return sum((num for num in integers[start:end + 1] if num % 2 == 0))