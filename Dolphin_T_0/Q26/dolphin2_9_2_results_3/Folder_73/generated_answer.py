def sum_in_range(lst):
    result = 0
    for num in lst:
        if 20 <= num <= 93:
            result += num
    return result