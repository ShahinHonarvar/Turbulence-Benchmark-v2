def sum_in_range(lst):
    total = 0
    for number in lst:
        if number >= 113 and number <= 392:
            total += number
    return total if total != 0 else 0