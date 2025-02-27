def sum_in_range(lst):
    result = 0
    for i in lst:
        if 10 <= i <= 79:
            result += i
    return result