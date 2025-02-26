def filter_chars(s):
    filtered_chars = []
    for i, char in enumerate(s):
        if 12 <= i <= 25 and 'P' <= char <= 'x':
            continue
        filtered_chars.append(char)
    return ''.join(filtered_chars)