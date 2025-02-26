def filter_chars(string):
    result = []
    for i, char in enumerate(string):
        if 38 <= i <= 99 and 'A' <= char <= 'Q':
            result.append(char)
    filtered_string = ''.join((char for char in string if char not in result))
    return filtered_string