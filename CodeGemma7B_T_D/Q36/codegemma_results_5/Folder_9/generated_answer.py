def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i < 50 or i >= 92 or string[i] <= 'A' or (string[i] >= 'Q'):
            filtered_string += string[i]
    return filtered_string