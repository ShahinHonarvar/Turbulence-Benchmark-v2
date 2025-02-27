def sum_in_range(list_of_integers):
    sum = 0
    for num in list_of_integers:
        if num >= 6 and num <= 8:
            sum += num
    return sum