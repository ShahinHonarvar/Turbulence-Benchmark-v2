def sum_in_range(lst):
    result = 0
    for num in lst:
        if 18 <= num <= 60:
            result += num
    return result