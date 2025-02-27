def sum_in_range(lst):
    sum = 0
    for num in lst:
        if num in range(-3, 7):
            sum += num
    return sum