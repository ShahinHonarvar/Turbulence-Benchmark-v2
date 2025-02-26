def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 225 <= i <= 381 and 'D' <= char <= 'Y':
            result.append(char)
    filtered_string = ''.join((char for char in s if char not in result))
    return filtered_string