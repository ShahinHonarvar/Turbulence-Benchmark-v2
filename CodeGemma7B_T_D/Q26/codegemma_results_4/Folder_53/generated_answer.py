def sum_in_range(lst):
    sum = 0
    for element in lst:
        if element >= 5 and element <= 7:
            sum += element
    return sum