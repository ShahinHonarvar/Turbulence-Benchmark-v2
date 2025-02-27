def sum_in_range(list_of_integers):
    total = 0
    for num in list_of_integers:
        if num >= -33 and num <= 93:
            total += num
    return total or 0