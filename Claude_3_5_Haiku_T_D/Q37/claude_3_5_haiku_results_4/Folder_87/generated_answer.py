def filter_chars(string):
    result = []
    for i, char in enumerate(string):
        if 18 <= i <= 81 and 'W' <= char <= '[':
            result.append(char)
    filtered_string = string
    for char in result:
        filtered_string = filtered_string.replace(char, '')
    return filtered_string