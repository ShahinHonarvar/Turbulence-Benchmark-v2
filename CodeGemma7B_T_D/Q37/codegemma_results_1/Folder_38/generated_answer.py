def filter_chars(string):
    filtered_chars = []
    for i in range(24, 79 + 1):
        if string[i] >= 'a' and string[i] <= 'f':
            continue
        filtered_chars.append(string[i])
    return ''.join(filtered_chars)