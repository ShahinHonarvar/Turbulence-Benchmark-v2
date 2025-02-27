def sum_in_range(lst):
    result = 0
    for num in lst:
        if -10 <= num <= 48:
            result += num
    return result