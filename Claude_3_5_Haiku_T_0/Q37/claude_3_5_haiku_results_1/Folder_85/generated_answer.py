def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 28 <= i <= 65 and 'O' <= char <= 'd':
            result.append(char)
    filtered_string = ''.join((char for char in s if char not in result))
    return filtered_string