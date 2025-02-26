def filter_chars(s):
    filtered_chars = []
    for i, char in enumerate(s):
        if 32 <= i <= 46 and '0' <= char <= 'k':
            continue
        filtered_chars.append(char)
    return ''.join(filtered_chars)