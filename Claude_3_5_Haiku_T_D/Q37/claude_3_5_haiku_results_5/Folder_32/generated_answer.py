def filter_chars(string):
    result = []
    for i, char in enumerate(string):
        if 23 <= i <= 89 and 'w' <= char <= '{':
            result.append(char)
    filtered_string = ''.join((char for char in string if char not in result))
    return filtered_string