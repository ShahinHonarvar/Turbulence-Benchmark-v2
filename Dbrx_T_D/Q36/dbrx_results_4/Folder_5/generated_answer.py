def filter_chars(s):
    filtered_s = ''
    for i, char in enumerate(s):
        if 55 < i < 66 and 'f' < char < '|':
            filtered_s = filtered_s.replace(char, '')
        else:
            filtered_s += char
    return filtered_s