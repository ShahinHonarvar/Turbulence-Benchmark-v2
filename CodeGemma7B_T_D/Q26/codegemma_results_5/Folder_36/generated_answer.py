def sum_in_range(lst):
    result = 0
    for i in lst:
        if i >= 465 and i <= 927:
            result += i
    return result if result else 0