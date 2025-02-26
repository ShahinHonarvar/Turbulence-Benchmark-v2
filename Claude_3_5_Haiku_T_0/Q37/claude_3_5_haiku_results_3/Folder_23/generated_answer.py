def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 51 <= i <= 77 and 'V' <= char <= 'Y':
            result.append(char)
    filtered_string = ''.join((char for char in s if char not in result))
    return filtered_string