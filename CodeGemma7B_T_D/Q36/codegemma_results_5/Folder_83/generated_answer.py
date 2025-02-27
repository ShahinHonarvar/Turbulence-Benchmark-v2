def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i >= 72 and i < 93 and (string[i] > '<') and (string[i] < 'J'):
            continue
        filtered_string += string[i]
    return filtered_string