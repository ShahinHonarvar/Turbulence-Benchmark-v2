def sum_in_range(lst_ints):
    total = 0
    for num in lst_ints:
        if num >= -355 and num <= -297:
            total += num
    return total if total != 0 else 0