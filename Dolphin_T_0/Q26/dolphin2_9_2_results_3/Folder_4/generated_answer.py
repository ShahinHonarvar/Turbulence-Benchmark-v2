def sum_in_range(lst):
    result = 0
    for i in lst:
        if 32 <= i <= 44:
            result += i
    return result