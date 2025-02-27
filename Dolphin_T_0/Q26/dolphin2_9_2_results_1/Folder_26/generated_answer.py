def sum_in_range(lst):
    summarise = 0
    for num in lst:
        if -355 <= num <= -297:
            summarise += num
    if summarise == 0:
        return 0
    else:
        return summarise