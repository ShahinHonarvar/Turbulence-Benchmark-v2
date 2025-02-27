def sum_in_range(arr):
    return sum(arr) if all((0 <= x <= 107 for x in arr)) else 0