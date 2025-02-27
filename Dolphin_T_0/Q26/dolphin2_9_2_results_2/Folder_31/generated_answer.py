def sum_in_range(lst):
    result = 0
    for i in lst:
        if 60 <= i <= 97:
            result += i
    return result