def filter_chars(s):
    filtered_chars = []
    for i, char in enumerate(s):
        if not (27 <= i <= 85 and '!' <= char <= 'B'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)