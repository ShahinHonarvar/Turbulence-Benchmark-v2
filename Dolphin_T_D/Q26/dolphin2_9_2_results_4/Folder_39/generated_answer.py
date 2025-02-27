def sum_in_range(lst):
    result = 0
    for num in lst:
        if 10 <= num <= 79:
            result += num
    return result