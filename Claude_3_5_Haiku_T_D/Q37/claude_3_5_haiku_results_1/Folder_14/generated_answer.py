def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 35 <= i <= 98 and 'A' <= char <= 'b':
            result.append(char)
    filtered_string = ''.join((char for char in s if char not in result))
    return filtered_string