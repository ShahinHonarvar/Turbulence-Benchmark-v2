def sum_in_range(lst):
    result = 0
    for num in lst:
        if -8 <= num <= 8:
            result += num
    return result