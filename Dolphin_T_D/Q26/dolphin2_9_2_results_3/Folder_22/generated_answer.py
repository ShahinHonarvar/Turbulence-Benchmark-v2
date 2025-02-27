def sum_in_range(lst):
    result = 0
    for i in lst:
        if 4 <= i <= 6:
            result += i
    return result