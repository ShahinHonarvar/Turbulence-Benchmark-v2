def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 1 <= i <= 5 and '$' <= char <= ';':
            result.append(char)
    filtered = ''
    for char in s:
        if char not in result:
            filtered += char
    return filtered