def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 29 <= i <= 79 and 'K' <= char <= 'z':
            result.append(char)
    filtered_string = ''.join((char for char in s if char not in result))
    return filtered_string