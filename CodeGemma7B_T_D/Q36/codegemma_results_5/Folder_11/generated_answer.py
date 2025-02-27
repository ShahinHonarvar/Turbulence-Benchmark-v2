def filter_chars(s):
    filtered_string = ''
    for i in range(86, 93):
        if s[i] > 'E' and s[i] < '~':
            filtered_string += ''
        else:
            filtered_string += s[i]
    return filtered_string