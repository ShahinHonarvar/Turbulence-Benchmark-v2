def sum_in_range(l):
    result = 0
    for i in l:
        if -8 <= i <= 8:
            result += i
    return result