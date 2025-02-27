def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i < 27 or i >= 75 or (not (string[i] > 'A' and string[i] < 'i')):
            filtered_string += string[i]
    return filtered_string