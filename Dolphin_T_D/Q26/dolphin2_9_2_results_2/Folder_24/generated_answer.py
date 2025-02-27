def sum_in_range(lst):
    result = 0
    for num in lst:
        if -91 <= num <= -41:
            result += num
    return result