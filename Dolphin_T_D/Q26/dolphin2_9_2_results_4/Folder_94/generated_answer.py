def sum_in_range(lst):
    result = 0
    for number in lst:
        if 36 <= number <= 52:
            result += number
    return result