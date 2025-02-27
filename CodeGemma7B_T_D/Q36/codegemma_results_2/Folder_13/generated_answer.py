def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i < 323 or i >= 526 or string[i] <= ')' or (string[i] >= 'O'):
            filtered_string += string[i]
    return filtered_string