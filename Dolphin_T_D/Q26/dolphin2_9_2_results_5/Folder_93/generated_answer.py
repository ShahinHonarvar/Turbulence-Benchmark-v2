def sum_in_range(lst):
    result = 0
    for i in lst:
        if -23 <= i <= 64:
            result += i
    return result