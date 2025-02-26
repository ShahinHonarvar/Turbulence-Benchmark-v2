def filter_chars(text):
    filtered_chars = []
    for i, char in enumerate(text):
        if 52 <= i <= 81 and 'A' <= char <= 'U':
            continue
        filtered_chars.append(char)
    return ''.join(filtered_chars)