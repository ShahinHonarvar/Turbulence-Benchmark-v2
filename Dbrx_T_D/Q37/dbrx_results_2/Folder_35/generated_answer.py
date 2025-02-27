def filter_chars(s):
    filtered_chars = []
    for i, char in enumerate(s):
        if i < 155 or i > 403:
            filtered_chars.append(char)
        elif char >= '(' and char <= ']':
            continue
        else:
            filtered_chars.append(char)
    return ''.join(filtered_chars)