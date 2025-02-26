def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 27 <= i <= 85 and '!' <= char <= 'B':
            result.append(char)
    filtered = []
    for char in s:
        if char not in result:
            filtered.append(char)
    return ''.join(filtered)