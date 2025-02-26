def filter_chars(input_string):
    result = []
    for i, char in enumerate(input_string):
        if 63 <= i <= 84 and 'E' <= char <= '~':
            result.append(char)
    filtered_string = input_string
    for char in result:
        filtered_string = filtered_string.replace(char, '')
    return filtered_string