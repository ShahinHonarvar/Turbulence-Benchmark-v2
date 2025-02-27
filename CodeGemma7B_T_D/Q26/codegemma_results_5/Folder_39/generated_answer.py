def sum_in_range(lst):
    sum = 0
    for num in lst:
        if num >= 10 and num <= 79:
            sum = sum + num
    return sum