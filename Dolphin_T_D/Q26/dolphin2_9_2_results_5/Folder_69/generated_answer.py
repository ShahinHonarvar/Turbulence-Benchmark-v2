def sum_in_range(lst):
    total = 0
    for i in lst:
        if 739 <= i <= 928:
            total += i
    return total if total > 0 else 0