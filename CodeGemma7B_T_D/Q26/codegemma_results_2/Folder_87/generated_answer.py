def sum_in_range(lst):
    result = 0
    for number in lst:
        if 60 <= number <= 90:
            result += number
    return result or 0