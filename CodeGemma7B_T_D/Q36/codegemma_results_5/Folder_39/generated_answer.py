def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i < 43 or i >= 59 or string[i] <= '5' or (string[i] >= 'C'):
            filtered_string += string[i]
    return filtered_string