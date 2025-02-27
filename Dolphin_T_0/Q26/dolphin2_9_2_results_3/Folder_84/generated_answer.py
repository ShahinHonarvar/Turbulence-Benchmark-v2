def sum_in_range(lst):
    result = 0
    for num in lst:
        if 113 <= num <= 392:
            result += num
    return result if result != 0 else None