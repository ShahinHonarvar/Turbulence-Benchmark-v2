def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 10 <= i <= 69 and 'I' <= char <= 'K':
            result.append(char)
    filtered = ''.join((char for char in s if char not in result))
    return filtered