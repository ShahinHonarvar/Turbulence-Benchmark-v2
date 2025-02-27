def sum_in_range(lst):
    sum = 0
    for element in lst:
        if element >= 60 and element <= 97:
            sum += element
    return sum