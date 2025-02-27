def sum_in_range(lst):
    result = 0
    for num in lst:
        if 142 <= num <= 980:
            result += num
    return result if result else 0