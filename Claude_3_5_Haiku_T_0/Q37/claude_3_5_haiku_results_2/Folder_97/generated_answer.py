def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 227 <= i <= 235 and 'D' <= char <= 'u':
            result.append(char)
    filtered_string = ''.join((char for char in s if char not in result))
    return filtered_string