def sum_in_range(lst):
    result = 0
    for i in lst:
        if -9 <= i <= -7:
            result += i
    return result if result != 0 else 0