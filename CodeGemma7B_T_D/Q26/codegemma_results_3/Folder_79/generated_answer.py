def sum_in_range(lst):
    sum = 0
    for i in lst:
        if i >= 2 and i <= 9:
            sum += i
            return sum