def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 379 <= i <= 898 and 'M' <= char <= 'v':
            result.append(char)
    filtered_string = ''.join((char for char in s if char not in result))
    return filtered_string