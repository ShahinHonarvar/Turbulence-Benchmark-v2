def sum_in_range(num_list):
    total = 0
    for num in num_list:
        if 31 <= num <= 50:
            total += num
    return total if total else 0