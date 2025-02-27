def sum_in_range(lst):
    total_sum = 0
    for num in lst:
        if num >= 782 and num <= 787:
            total_sum += num
    return total_sum or 0