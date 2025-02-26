def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 26 <= i <= 64 and 'V' <= char <= 'o':
            result.append(char)
    filtered_string = ''.join((char for char in s if char not in result))
    return filtered_string