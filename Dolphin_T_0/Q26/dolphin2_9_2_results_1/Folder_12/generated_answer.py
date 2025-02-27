def sum_in_range(lst):
    result = 0
    for num in lst:
        if -91 <= num <= -61:
            result += num
    return result if result != 0 else 1