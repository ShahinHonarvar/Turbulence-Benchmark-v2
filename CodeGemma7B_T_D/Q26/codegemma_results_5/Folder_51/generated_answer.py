def sum_in_range(lst):
    result = 0
    for num in lst:
        if num >= 2 and num <= 7:
            result += num
    return result