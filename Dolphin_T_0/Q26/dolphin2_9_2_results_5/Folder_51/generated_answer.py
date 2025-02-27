def sum_in_range(lst):
    result = 0
    for num in lst:
        if 2 <= num <= 7:
            result += num
    return result