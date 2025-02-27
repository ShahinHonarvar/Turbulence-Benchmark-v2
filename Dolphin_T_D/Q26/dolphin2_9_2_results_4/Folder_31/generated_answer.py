def sum_in_range(lst):
    total_sum = 0
    for num in lst:
        if 60 <= num <= 97:
            total_sum += num
    return total_sum