def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i >= 54 and i <= 92 and (string[i] > 'J') and (string[i] < 'X'):
            continue
        filtered_string += string[i]
    return filtered_string