def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i >= 36 and i <= 79 and ('a' <= string[i] <= 'i'):
            continue
        filtered_string += string[i]
    return filtered_string