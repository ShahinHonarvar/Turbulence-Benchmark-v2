def sum_in_range(lst):
    total_sum = 0
    for num in lst:
        if num >= 5 and num <= 9:
            total_sum += num
    return total_sum