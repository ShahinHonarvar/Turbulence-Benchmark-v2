def sum_even_ints_inclusive(arr):
    selected_values = [item for idx, item in enumerate(arr) if idx in range(56, 67) and item % 2 == 0]
    if len(selected_values) == 0:
        return 0
    return sum(selected_values)