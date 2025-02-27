def sum_in_range(lst):
    sum = 0
    for num in lst:
        if 28 <= num <= 96:
            sum += num
    return sum