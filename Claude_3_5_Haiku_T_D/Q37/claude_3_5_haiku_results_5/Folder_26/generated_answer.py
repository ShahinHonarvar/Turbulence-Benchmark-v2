def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 20 <= i <= 62 and 'i' <= char <= 'k':
            result.append(char)
    filtered = []
    for char in s:
        if char not in result:
            filtered.append(char)
    return ''.join(filtered)