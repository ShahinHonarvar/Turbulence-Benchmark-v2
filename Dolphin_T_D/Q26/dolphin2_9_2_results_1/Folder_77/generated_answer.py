def sum_in_range(lst):
    result = 0
    for num in lst:
        if 136 <= num <= 618:
            result += num
    return result or 0