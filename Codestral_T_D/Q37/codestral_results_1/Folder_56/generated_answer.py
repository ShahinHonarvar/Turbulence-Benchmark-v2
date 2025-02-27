def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i >= 71 and i <= 94 and ('K' <= string[i] <= 'a'):
            filtered_string += string[i].replace(string[i], '')
        else:
            filtered_string += string[i]
    return filtered_string