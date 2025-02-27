def sum_in_range(lst):
    result = 0
    for num in lst:
        if 3 <= num <= 4:
            result += num
    return result