def filter_chars(s):
    filtered_chars = []
    for i, char in enumerate(s):
        if 10 <= i <= 52 and '@' <= char <= 'T':
            continue
        filtered_chars.append(char)
    return ''.join(filtered_chars)