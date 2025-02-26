def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 35 <= i <= 98 and 'A' <= char <= 'b':
            result.append(char)
    filtered_chars = []
    for char in s:
        if char not in result:
            filtered_chars.append(char)
    return ''.join(filtered_chars)