def sum_in_range(lst):
    sum = 0
    for num in lst:
        if 31 <= num <= 50:
            sum += num
    return sum