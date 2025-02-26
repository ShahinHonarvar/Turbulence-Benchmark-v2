def sum_odd_ints_inclusive(integers):
    if len(integers) <= 68:
        return 0
    end_index = min(86, len(integers) - 1)
    return sum((num for num in integers[68:end_index + 1] if num % 2 != 0))