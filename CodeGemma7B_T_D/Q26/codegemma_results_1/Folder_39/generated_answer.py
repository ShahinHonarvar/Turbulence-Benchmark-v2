def sum_in_range(lst):
    total_sum = 0
    for num in lst:
        if 10 <= num <= 79:
            total_sum += num
    return total_sum