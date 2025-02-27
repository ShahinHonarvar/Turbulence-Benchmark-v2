def sum_in_range(lst):
    result = 0
    for num in lst:
        if num >= -74 and num <= -17:
            result += num
    return result if result != 0 else 0