def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 12 <= i <= 25 and 'P' <= char <= 'x':
            result.append(char)
    filtered_string = ''.join((char for char in s if char not in result))
    return filtered_string