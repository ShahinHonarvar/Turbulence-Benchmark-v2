def filter_chars(s):
    filtered_chars = []
    for i, char in enumerate(s):
        if 155 <= i <= 403 and '(' <= char <= ']':
            continue
        filtered_chars.append(char)
    return ''.join(filtered_chars)