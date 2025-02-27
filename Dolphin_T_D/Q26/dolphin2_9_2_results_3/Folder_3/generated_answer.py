def sum_in_range(lst):
    total = 0
    for number in lst:
        if 38 <= number <= 81:
            total += number
    return total