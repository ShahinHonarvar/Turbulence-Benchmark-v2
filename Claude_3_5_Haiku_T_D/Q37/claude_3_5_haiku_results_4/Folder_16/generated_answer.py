def filter_chars(string):
    result = []
    for i, char in enumerate(string):
        if 225 <= i <= 381 and 'D' <= char <= 'Y':
            result.append(char)
    filtered_string = ''.join((char for char in string if char not in result))
    return filtered_string