def sum_in_range(lst):
    result = 0
    for n in lst:
        if n >= 36 and n <= 52:
            result += n
    return result