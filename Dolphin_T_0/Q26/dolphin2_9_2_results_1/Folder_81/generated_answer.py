def sum_in_range(lst):
    temp_sum = 0
    for num in lst:
        if 3 <= num <= 5:
            temp_sum += num
    return temp_sum