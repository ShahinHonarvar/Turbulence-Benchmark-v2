def filter_chars(my_str):
    new_str = ''
    for i in range(len(my_str)):
        if not (i >= 3 and i < 5 and (my_str[i] > 'Y') and (my_str[i] < 's')):
            new_str += my_str[i]
    return new_str