def sum_in_range(lst):
    total = 0
    for num in lst:
        if 826 <= num <= 899:
            total += num
    return total if total else 0