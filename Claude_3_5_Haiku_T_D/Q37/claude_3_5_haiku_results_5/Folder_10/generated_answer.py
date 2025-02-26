def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 63 <= i <= 84 and 'E' <= char <= '~':
            result.append(char)
    filtered_string = s
    for char in result:
        filtered_string = filtered_string.replace(char, '')
    return filtered_string