def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 27 <= i <= 85 and 'c' <= char <= 'i':
            result.append(char)
    filtered_string = ''.join((char for char in s if char not in result))
    return filtered_string