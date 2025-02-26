def sum_even_ints_inclusive(integers):
    start_index = 639
    end_index = 975
    if len(integers) <= start_index:
        return 0
    end_index = min(end_index, len(integers) - 1)
    total = 0
    for i in range(start_index, end_index + 1):
        if integers[i] % 2 == 0:
            total += integers[i]
    return total