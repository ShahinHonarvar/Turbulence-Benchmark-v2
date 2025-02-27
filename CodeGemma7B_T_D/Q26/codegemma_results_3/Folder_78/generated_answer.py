def sum_in_range(list):
    sum = 0
    for i in range(len(list)):
        if list[i] >= 90 and list[i] <= 97:
            sum += list[i]
    return sum