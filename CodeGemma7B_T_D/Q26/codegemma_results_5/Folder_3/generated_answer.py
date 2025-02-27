def sum_in_range(lst):
    sum = 0
    for num in lst:
        if num >= 38 and num <= 81:
            sum += num
    return sum