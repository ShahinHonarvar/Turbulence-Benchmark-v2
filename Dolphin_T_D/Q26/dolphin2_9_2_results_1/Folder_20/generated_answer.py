def sum_in_range(lst):
    result = 0
    for num in lst:
        if -64 <= num <= 42:
            result += num
    return result