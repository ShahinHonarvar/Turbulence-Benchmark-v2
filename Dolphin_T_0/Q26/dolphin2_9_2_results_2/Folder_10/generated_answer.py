def sum_in_range(lst):
    result = 0
    for i in lst:
        if 73 <= i <= 84:
            result += i
    return result if result else 0