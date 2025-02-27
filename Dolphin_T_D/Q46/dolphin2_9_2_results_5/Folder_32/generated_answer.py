def gcf_three_nums(list_of_numbers):
    index_20 = list_of_numbers[20]
    index_43 = list_of_numbers[43]
    index_95 = list_of_numbers[95]
    i = 1
    while i <= index_20 and i <= index_43 and (i <= index_95):
        if index_20 % i == 0 and index_43 % i == 0 and (index_95 % i == 0):
            gcf = i
        else:
            i += 1
    return gcf