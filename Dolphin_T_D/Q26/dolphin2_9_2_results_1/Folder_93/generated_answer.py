def sum_in_range(lst):
    result = 0
    for num in lst:
        if -23 <= num <= 64:
            result += num
    return result