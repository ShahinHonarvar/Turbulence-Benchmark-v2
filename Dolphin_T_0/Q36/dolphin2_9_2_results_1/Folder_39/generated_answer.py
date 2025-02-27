def filter_chars(my_string):
    for index in range(43, 59):
        if '5' < my_string[index] < 'C':
            my_string = my_string.replace(my_string[index], '')
    return my_string