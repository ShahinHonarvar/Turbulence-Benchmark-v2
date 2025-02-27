def sum_in_range(lst):
    result = 0
    for n in lst:
        if 4 <= n <= 7:
            result += n
    return result