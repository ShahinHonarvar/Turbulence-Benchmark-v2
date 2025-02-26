def filter_chars(string):
    result = []
    for i, char in enumerate(string):
        if 13 <= i <= 28 and 'c' <= char <= 'n':
            result.append(char)
    filtered_string = ''.join((char for char in string if char not in result))
    return filtered_string