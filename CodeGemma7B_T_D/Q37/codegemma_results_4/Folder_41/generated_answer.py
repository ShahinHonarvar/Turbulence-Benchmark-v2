def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i >= 26 and i <= 64 and (string[i] >= 'V') and (string[i] <= 'o'):
            continue
        filtered_string += string[i]
    return filtered_string