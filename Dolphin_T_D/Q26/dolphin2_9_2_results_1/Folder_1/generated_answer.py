def sum_in_range(lst):
    sum = 0
    for num in lst:
        if -97 <= num <= -48:
            sum += num
    return sum