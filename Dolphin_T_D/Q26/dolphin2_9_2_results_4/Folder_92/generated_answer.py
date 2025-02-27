def sum_in_range(integer_list):
    total = 0
    for num in integer_list:
        if 5 <= num <= 9:
            total += num
    return total if total else 0