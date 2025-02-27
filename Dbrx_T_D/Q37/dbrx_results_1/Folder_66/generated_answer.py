def filter_chars(s):
    filtered_s = ''
    for i, char in enumerate(s):
        if i >= 27 and i <= 85 and ('c' <= char <= 'i'):
            continue
        filtered_s += char
    return filtered_s