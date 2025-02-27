def sum_in_range(lst):
    result = 0
    for num in lst:
        if num in range(2, 8):
            result += num
    return result