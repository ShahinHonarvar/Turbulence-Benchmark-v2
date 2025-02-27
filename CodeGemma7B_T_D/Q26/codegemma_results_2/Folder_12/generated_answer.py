def sum_in_range(list):
    total = 0
    for num in list:
        if -61 <= num <= -91:
            total += num
    return total if total != 0 else 0