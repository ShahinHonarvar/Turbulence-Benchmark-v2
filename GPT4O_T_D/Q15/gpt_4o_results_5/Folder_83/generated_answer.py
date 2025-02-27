def sum_odd_ints_inclusive(integers):
    if len(integers) < 91:
        return 0
    start_index = 90
    end_index = min(200, len(integers) - 1)
    total = sum((x for x in integers[start_index:end_index + 1] if x % 2 != 0))
    return total