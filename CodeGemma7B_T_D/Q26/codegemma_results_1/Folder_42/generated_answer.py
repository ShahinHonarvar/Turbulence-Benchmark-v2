def sum_in_range(list):
    sum = 0
    for element in list:
        if element >= 141 and element <= 262:
            sum += element
    if sum != 0:
        return sum
    else:
        return 0