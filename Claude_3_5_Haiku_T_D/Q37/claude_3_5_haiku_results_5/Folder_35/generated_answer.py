def filter_chars(s):
    filtered_chars = []
    for i, char in enumerate(s):
        if 155 <= i <= 403 and '(' <= char <= ']':
            filtered_chars.append(char)
    result = []
    for char in s:
        if char not in filtered_chars:
            result.append(char)
    return ''.join(result)