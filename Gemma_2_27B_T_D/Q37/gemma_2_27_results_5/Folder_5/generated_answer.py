def filter_chars(s):
    filtered_string = ''
    for i, char in enumerate(s):
        if 24 <= i <= 82 and '5' <= char <= '<':
            s = s.replace(char, '')
        filtered_string += char
    return filtered_string