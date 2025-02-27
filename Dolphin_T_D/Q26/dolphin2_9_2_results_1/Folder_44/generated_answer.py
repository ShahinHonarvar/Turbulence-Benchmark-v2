def sum_in_range(lst):
    result = 0
    for number in lst:
        if -993 <= number <= -51:
            result += number
    return result if result > 0 else 0