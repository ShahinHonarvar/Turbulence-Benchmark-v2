def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 31 <= i <= 38 and ';' <= char <= 'g':
            result.append(char)
    filtered_string = ''.join((char for char in s if char not in result))
    return filtered_string