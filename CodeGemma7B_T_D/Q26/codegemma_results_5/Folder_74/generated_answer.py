def sum_in_range(list_of_ints):
    sum = 0
    for num in list_of_ints:
        if num in range(13, 36):
            sum += num
    return sum