def sum_in_range(lst):
    result = 0
    for i in lst:
        if -100 <= i <= -55:
            result += i
    return result