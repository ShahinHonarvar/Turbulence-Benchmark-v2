def sum_in_range(arr):
    total = 0
    for num in arr:
        if 31 <= num <= 50:
            total += num
    return total