def filter_chars(s):
    filtered_string = list(s)
    for i in range(669, 888):
        if s[i] > 'B' and s[i] < 'Y':
            while s[i] in filtered_string:
                filtered_string.remove(s[i])
    return ''.join(filtered_string)