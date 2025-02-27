def sum_in_range(lst):
    result = 0
    for i in lst:
        if i >= 5 and i <= 8:
            result += i
    return result if result != 0 else 0