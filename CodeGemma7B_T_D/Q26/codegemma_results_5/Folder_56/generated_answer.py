def sum_in_range(lst):
    sum = 0
    for n in lst:
        if n >= 4 and n <= 9:
            sum += n
    return sum