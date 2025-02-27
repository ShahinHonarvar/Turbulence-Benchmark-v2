def sum_in_range(lst):
    result = 0
    for i in lst:
        if 2 <= i <= 4:
            result += i
    return result