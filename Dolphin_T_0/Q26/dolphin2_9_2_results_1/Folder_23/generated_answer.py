def sum_in_range(lst):
    result = 0
    for num in lst:
        if 50 <= num <= 92:
            result += num
    return result