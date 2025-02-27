def sum_in_range(lst):
    result = 0
    for i in lst:
        if 6 <= i <= 9:
            result += i
    if result == 0:
        return 0
    else:
        return result