def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i >= 587 and i <= 648 and (string[i] > ',') and (string[i] < 'c'):
            continue
        else:
            filtered_string += string[i]
    return filtered_string