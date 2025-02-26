def sum_even_ints_inclusive(integers):
    start_index = max(667, 0)
    end_index = min(774, len(integers) - 1)
    return sum((num for num in integers[start_index:end_index + 1] if num % 2 == 0))