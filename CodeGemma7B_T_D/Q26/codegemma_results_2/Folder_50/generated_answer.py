def sum_in_range(lst):
    sum = 0
    start = 34
    end = 69
    for num in lst:
        if start <= num <= end:
            sum += num
    return sum