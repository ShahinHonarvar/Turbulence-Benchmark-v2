def filter_chars(s):
    filtered_chars = []
    for i, char in enumerate(s):
        if 27 <= i <= 85 and '!' <= char <= 'B':
            continue
        filtered_chars.append(char)
    return ''.join(filtered_chars)