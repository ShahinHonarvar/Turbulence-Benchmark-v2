def sum_in_range(lst):
    result = 0
    for num in lst:
        if 60 <= num <= 97:
            result += num
    return result