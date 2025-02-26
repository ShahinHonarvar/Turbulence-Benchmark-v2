def sum_even_ints_inclusive(integers):
    start = max(639, 0)
    end = min(975, len(integers) - 1)
    return sum((num for num in integers[start:end + 1] if num % 2 == 0))