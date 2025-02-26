def filter_chars(s):
    filtered_chars = []
    for i, char in enumerate(s):
        if 515 <= i <= 538 and '+' <= char <= '}':
            continue
        filtered_chars.append(char)
    return ''.join(filtered_chars)