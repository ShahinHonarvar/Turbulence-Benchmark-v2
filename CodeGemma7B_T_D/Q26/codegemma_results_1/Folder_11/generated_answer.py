def sum_in_range(list):
    sum = 0
    for n in list:
        if n in range(11, 77):
            sum += n
    return sum