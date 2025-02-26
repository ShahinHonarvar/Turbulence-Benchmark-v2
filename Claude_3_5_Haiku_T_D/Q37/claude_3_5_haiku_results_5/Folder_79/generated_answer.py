def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 10 <= i <= 52 and '@' <= char <= 'T':
            result.append(char)
    filtered = []
    for char in s:
        if char not in result:
            filtered.append(char)
    return ''.join(filtered)