def sum_in_range(lst):
    result = 0
    for i in lst:
        if -8 <= i <= 8:
            result += i
    return result