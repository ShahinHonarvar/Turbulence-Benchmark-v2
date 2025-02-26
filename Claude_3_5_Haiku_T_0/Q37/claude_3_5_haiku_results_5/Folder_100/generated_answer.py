def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 88 <= i <= 90 and 'J' <= char <= 'Q':
            result.append(char)
    filtered_string = ''.join((char for char in s if char not in result))
    return filtered_string