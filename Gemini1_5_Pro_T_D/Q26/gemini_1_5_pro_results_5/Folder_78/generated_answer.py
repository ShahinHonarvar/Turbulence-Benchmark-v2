def sum_in_range(input_list):
    sum = 0
    for element in input_list:
        if element >= 90 and element <= 97:
            sum += element
    return sum