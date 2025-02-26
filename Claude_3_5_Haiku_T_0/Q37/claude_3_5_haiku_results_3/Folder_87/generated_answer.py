def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 18 <= i <= 81 and 'W' <= char <= '[':
            result.append(char)
    filtered_string = ''.join((char for char in s if char not in result))
    return filtered_string