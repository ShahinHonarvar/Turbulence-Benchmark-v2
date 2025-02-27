def sum_in_range(lst):
    result = 0
    for integer in lst:
        if -33 <= integer <= 93:
            result += integer
    return result if result else 0