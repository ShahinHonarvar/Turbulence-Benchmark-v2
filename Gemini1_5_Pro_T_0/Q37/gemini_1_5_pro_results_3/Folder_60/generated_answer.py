def filter_chars(s):
    filtered_string = ''
    for i, char in enumerate(s):
        if i in range(12, 78) and ':' <= char <= 'L':
            s = s.replace(char, '')
        filtered_string += s[i]
    return filtered_string